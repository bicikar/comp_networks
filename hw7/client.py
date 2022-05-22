import datetime
from socket import socket, AF_INET, SOCK_DGRAM, timeout

TIMEOUT = 1
IP = 'localhost'
PORT = 49233
BUFF_SIZE = 1024

if __name__ == '__main__':
    with socket(AF_INET, SOCK_DGRAM) as udp_socket:
        udp_socket.connect((IP, PORT))
        udp_socket.settimeout(TIMEOUT)
        rtts = []
        for seq_num in range(10):
            start = datetime.datetime.now()
            message = 'Ping seq_number={seq_number} time={time}'
            msg_to_send = message.format(seq_number=seq_num,
                                         time=start).encode()
            udp_socket.sendall(msg_to_send)
            try:
                data = udp_socket.recv(BUFF_SIZE)
                rtts.append((datetime.datetime.now() - start).microseconds)
                print(data.decode())
            except timeout:
                pass
        loss = (1 - len(rtts) / 10.0) * 100
        print(f'10 packets transmitted, {len(rtts)} received, {round(loss, 2)}% pocket_loss')
        print(f'rtt min-max-avg = {min(rtts)}-{max(rtts)}-{round(sum(rtts)/len(rtts), 2)}')
