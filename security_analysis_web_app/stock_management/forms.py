from django import forms

from .views import StockController

class NewStockForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=10)
    stockController = StockController

    def __init__(self, request=None):
        super(NewStockForm,self).__init__(request)

        if request is not None:
            self.is_valid()

            self.ticker = self.cleaned_data['ticker']
            self.stockController = StockController(self.ticker)

    def update(self):
        self.stockController.update()
