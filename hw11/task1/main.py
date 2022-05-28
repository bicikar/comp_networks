from socket import *
import socket
import os
import sys
import struct
import time
import select

from checksums import checksum
ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2
TRIES = 2


def build_packet():
    myChecksum = 0
    myID = os.getpid() & 0xFFFF

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1)
    data = struct.pack("d", time.time())

    myChecksum = checksum(header + data)
    if sys.platform == 'darwin':
        myChecksum = socket.htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1)
    packet = header + data
    return packet


def get_route(hostname):
    timeLeft = TIMEOUT
    for ttl in range(1, MAX_HOPS):
        for tries in range(TRIES):
            destAddr = socket.gethostbyname(hostname)
            icmp = socket.getprotobyname("icmp")
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

            mySocket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL,
                                struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)
            try:
                d = build_packet()
                mySocket.sendto(d, (hostname, 0))
                t = time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)
                if whatReady[0] == []:  # Timeout
                    print(f'{"*    " * TRIES}Request timed out.')

                recvPacket, addr = mySocket.recvfrom(1024)
                print(addr)
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect
                if timeLeft <= 0:
                    print("*    *    * Request timed out.")
                    return
            except socket.timeout:
                continue
            else:
                icmpHeader = recvPacket[20:28]
                request_type, code, checksum, packetID, sequence = struct.unpack(
                    "bbHHh", icmpHeader)
                if request_type == 11:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print("TTL %d   rtt=%.0f ms %s" % (
                        ttl, (timeReceived - t) * 1000, addr[0]))
                elif request_type == 3:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print("TTL %d   rtt=%.0f ms %s" % (
                        ttl, (timeReceived - t) * 1000, addr[0]))
                elif request_type == 0:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print(
                        "rtt=%.0f ms %s" % (
                            (timeReceived - timeSent) * 1000, addr[0]))
                    return
                else:
                    print("error")
                    break
            finally:
                mySocket.close()


if __name__ == '__main__':
    get_route(sys.argv[1])
