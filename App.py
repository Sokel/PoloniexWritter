import daemon
import os

if __name__ == '__main__':
    print('program start')
    with daemon.DaemonContext():
        print(123)

    print('end')
