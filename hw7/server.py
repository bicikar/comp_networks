import datetime
import threading
import time

from socket import socket, AF_INET, SOCK_DGRAM

IP = 'localhost'
PORT = 49235
BUFF_SIZE = 1024

clients = {}
lock = threading.RLock()


def heartbeat(wait):
    while True:
        with lock:
            for addr in list(clients):
                last = clients[addr][1]
                delta = (datetime.datetime.now() - last).seconds
                if delta >= wait:
                    print(f'{addr} is no longer responding')
                    clients.pop(addr)
        time.sleep(0.1)


if __name__ == '__main__':
    threading.Timer(0.1, heartbeat, args=[2]).start()

    addr = (IP, PORT)
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(addr)
    while True:
        data, addr = udp_socket.recvfrom(BUFF_SIZE)
        arrival = datetime.datetime.now()
        data = data.decode().split()
        seq_number = int(data[0])
        sent = datetime.datetime.strptime(' '.join(data[1:]), '%Y-%m-%d %H:%M:%S.%f')

        with lock:
            if addr in clients:
                last = clients[addr][0]
                while last + 1 < seq_number:
                    last += 1
                    print(f'{addr} seq_number={last} LOST')
            clients[addr] = (seq_number, sent)
        print(f'{addr} seq_number={seq_number} time={(arrival - sent).microseconds} ms')
