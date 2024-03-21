import yfinance as yf
import datetime
from enum import Enum
from .models import FuturePrice


class Interval(Enum):
    wk1: str = "1wk"
    mo1: str = "1mo"
    mo3: str = "3mo"

    def __str__(self):
        return self.value

def fetch_future_prices(ticker_symbol: str, interval: Interval, start_date: datetime.date, end_date: datetime.date ) -> list[FuturePrice]:
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period=period, interval=interval)

    future_prices = []
    for date, row in hist.iterrows():
        future_prices.append(FuturePrice(
            date=date.strftime("%Y-%m-%d"),            
            close=row['Close'],

        ))

    return future_prices
