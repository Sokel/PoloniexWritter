from app.PoloniexWrapper import *


def main_context():
    wrapper = PoloniexWrapper()
    print(wrapper.get_ticker())


if __name__ == '__main__':
    while True:
        main_context()
