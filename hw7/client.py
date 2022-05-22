import datetime
import random
import sys
import time
from socket import socket, AF_INET, SOCK_DGRAM, timeout

TIMEOUT = 1
IP = 'localhost'
PORT = 49235
BUFF_SIZE = 1024

if __name__ == '__main__':
    port = int(sys.argv[1])
    with socket(AF_INET, SOCK_DGRAM) as udp_socket:
        udp_socket.bind((IP, port))
        udp_socket.connect((IP, PORT))
        udp_socket.settimeout(TIMEOUT)
        seq_num = 0
        while True:
            seq_num += 1
            time.sleep(0.5)
            if random.randint(1, 5) == 1:
                continue
            start = datetime.datetime.now()
            message = '{seq_number} {time}'
            msg_to_send = message.format(seq_number=seq_num,
                                         time=start).encode()
            udp_socket.sendall(msg_to_send)
