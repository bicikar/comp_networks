import datetime
import random
import socket

import config
from checksum import create_sum, check_sum


class StopAndWaitTimeOutException(Exception):
    pass


class StopAndWait:
    def __init__(self, src, dst):
        self.send_state = b'0'
        self.receive_state = b'0'
        self.resend_timeout = config.RESEND_TIMEOUT
        self.send_timeout = config.SEND_TIMEOUT
        self.receive_timeout = config.RECEIVE_TIMEOUT
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(src)
        self.udp_socket.connect(dst)

    def _send(self, data):
        data = data + format(create_sum(data),
                             '16d').encode() + self.send_state
        assert len(data) <= config.BUFF_SIZE
        self.udp_socket.settimeout(self.resend_timeout)
        start = datetime.datetime.now()
        while True:
            self.udp_socket.sendall(data)
            if (datetime.datetime.now() - start).seconds > self.send_timeout:
                raise StopAndWaitTimeOutException()
            try:
                received_data = self.udp_socket.recv(config.BUFF_SIZE)
                if random.randint(1, 10) <= 3:
                    continue
                assert len(received_data) == 1
                if received_data[0:] != self.send_state:
                    self.udp_socket.sendall(data)
                    continue
                break
            except socket.timeout:
                continue
        self.send_state = self.flip(self.send_state)

    @staticmethod
    def flip(state):
        return b'1' if state == b'0' else b'0'

    def send(self, data):
        size = config.BUFF_SIZE - 16 - 1
        parts = [data[i:i + size] for i in
                 range(0, len(data), size)]
        for part in parts:
            self._send(part)

    def receive(self):
        self.udp_socket.settimeout(self.receive_timeout)
        while True:
            try:
                data, _ = self.udp_socket.recvfrom(config.BUFF_SIZE)
                if random.randint(1, 10) <= 3:
                    continue
                sum_ = int(data[-17:-1])
                real_data = data[:-17]
                if (data[-1:] != self.receive_state or
                        not check_sum(calculated_sum=sum_,
                                      data=real_data)):
                    self.udp_socket.sendall(
                        self.flip(self.receive_state))
                else:
                    self.udp_socket.sendall(self.receive_state)
                    self.receive_state = self.flip(
                        self.receive_state)
                    return real_data
            except socket.timeout:
                raise StopAndWaitTimeOutException()
