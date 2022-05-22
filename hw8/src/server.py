import config
from stop_and_wait import StopAndWait, StopAndWaitTimeOutException

PATH_TO_TEXT = 'texts'

if __name__ == '__main__':
    saw = StopAndWait(
        src=('localhost', config.SERVER_PORT),
        dst=('localhost', config.CLIENT_PORT)
    )
    data = b''
    while True:
        try:
            data += saw.receive()
        except StopAndWaitTimeOutException:
            break
    with open(f'{PATH_TO_TEXT}/copy_alice.txt', 'wb') as file:
        file.write(data)
