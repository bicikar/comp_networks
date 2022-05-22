import random
from socket import socket, AF_INET, SOCK_DGRAM

IP = 'localhost'
PORT = 49233
BUFF_SIZE = 1024

if __name__ == '__main__':
    random.seed()
    addr = (IP, PORT)
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(addr)
    while True:
        data, addr = udp_socket.recvfrom(BUFF_SIZE)
        if random.randint(1, 5) == 1:
            continue
        upper_case_data = data.decode().upper().encode()
        udp_socket.sendto(upper_case_data, addr)
