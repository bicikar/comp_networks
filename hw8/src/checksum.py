import config

def create_sum(data):
    assert len(data) <= config.BUFF_SIZE
    return int.from_bytes(data, 'little') % config.MOD


def check_sum(calculated_sum, data):
    return create_sum(data) - calculated_sum == 0