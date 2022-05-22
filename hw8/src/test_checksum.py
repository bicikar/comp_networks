import random

from checksum import create_sum, check_sum
import config


def test_correct():
    data = b'10!'
    correct_sum = 2175025
    assert check_sum(calculated_sum=correct_sum, data=data)


def test_wrong():
    data = b'10!'
    correct_sum = 2175025 + random.randint(0, 199999999)
    assert not check_sum(calculated_sum=correct_sum, data=data)


def test_overflow():
    data = b'a' * 1024
    assert create_sum(data) <= config.MOD
