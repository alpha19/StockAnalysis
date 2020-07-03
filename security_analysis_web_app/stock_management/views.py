from django.shortcuts import render

from .models import Stock

import yfinance as yf
import finnhub
from finnhub.rest import ApiException

import keys

# Create your views here.

# This is basically a controller. Does it belong here???
class StockController:
    stock = Stock()

    def __init__(self, ticker: str):
        self.getStockObject(ticker)

    def getStockObject(self, ticker):
        try:
            self.stock = Stock.objects.get(pk=ticker)
        except Stock.DoesNotExist:
            self.stock = Stock(ticker_symbol=ticker)

    def update(self):
        self.queryForNewData()
        self.stock.save()

    # Updates the data via REST call for the given stock
    def queryForNewData(self):
        stockQuery = yf.Ticker(self.stock.ticker_symbol)
        finnData = self.getQuote()

        self.stock.price = finnData.c

        # Fill out the rest of the required data
        self.stock.ticker_symbol = stockQuery.info['symbol']
        self.stock.company_name = stockQuery.info['longName']
        self.stock.daily_change = finnData.c - finnData.o
        self.stock.daily_percent = 100 * (self.stock.daily_change / finnData.o)
        self.stock.year_high = stockQuery.info['fiftyTwoWeekHigh']
        self.stock.year_low = stockQuery.info['fiftyTwoWeekLow']

        # TODO: Is this still even relevant/worth it?
        self.stock.streak = 0

        return

    # Queries REST API
    def getQuote(self):
        # Configure API key
        configuration = finnhub.Configuration( api_key = { 'token': keys.FINNHUB_KEY } )

        with finnhub.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = finnhub.DefaultApi(api_client)

            try:
                # Aggregate Indicators
                return api_instance.quote(self.stock.ticker_symbol)
            except ApiException as e:
                print("Exception when calling DefaultApi->aggregate_indicator: %s\n" % e)

        return None
