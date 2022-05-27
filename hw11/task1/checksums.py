import sys
from socket import *


def checksum(source_string):
    countTo = (int(len(source_string) / 2)) * 2
    sum = 0
    count = 0

    loByte = 0
    hiByte = 0
    while count < countTo:
        if (sys.byteorder == "little"):
            loByte = source_string[count]
            hiByte = source_string[count + 1]
        else:
            loByte = source_string[count + 1]
            hiByte = source_string[count]

        sum = sum + (hiByte * 256 + loByte)
        count += 2

    if countTo < len(source_string):
        loByte = source_string[len(source_string) - 1]
        sum += loByte

    sum &= 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum += (sum >> 16)
    answer = ~sum & 0xffff
    answer = htons(answer)

    return answer
