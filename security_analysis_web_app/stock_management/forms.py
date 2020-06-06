from django import forms

from .models import Stock

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
        # TODO: Implementation
        return

    # Queries REST API
    def query(self):
        # TODO: Implementation
        return