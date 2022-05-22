import config

from stop_and_wait import StopAndWait

PATH_TO_TEXT = 'texts'

if __name__ == '__main__':
    saw = StopAndWait(
        src=('localhost', config.CLIENT_PORT),
        dst=('localhost', config.SERVER_PORT)
    )
    with open(f'{PATH_TO_TEXT}/alice.txt', 'rb') as f:
        data = f.read()
        saw.send(data=data)
