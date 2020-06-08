from django import forms

from .models import Stock
import keys

import yfinance as yf
import finnhub
from finnhub.rest import ApiException

class NewStockForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=10)

    def update(self):
        self.ticker = self.cleaned_data['ticker']

        # Check if in stocks db. If not, then create and update. Otherwise just update.
        stock = None
        try:
            stock = Stock.objects.get(pk=self.ticker)
        except Stock.DoesNotExist:
            stock = Stock(ticker_symbol=self.ticker)
        finally:
            self.queryForNewData(stock)
            stock.save()

    # Updates the data via REST call for the given stock
    def queryForNewData(self, stock):
        stockQuery = yf.Ticker(stock.ticker_symbol)
        finnData = self.queryQuote()

        stock.price = finnData.c

        # Fill out the rest of the required data

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
                return api_instance.quote(self.ticker)
            except ApiException as e:
                print("Exception when calling DefaultApi->aggregate_indicator: %s\n" % e)

        return None