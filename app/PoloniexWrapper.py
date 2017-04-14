from poloniex import Poloniex


class PoloniexWrapper:
    polo = Poloniex()

    def get_ticker(self):
        return self.polo.returnTicker()
