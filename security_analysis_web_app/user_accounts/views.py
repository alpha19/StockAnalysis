# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from ..stock_management.models import Stock
from ..stock_management.forms import NewStockForm

from django.shortcuts import render
from django.http import HttpResponse

def user_home(request):

    user = request.user
    num_stocks = user.profile.stocks.count()
    context = {
        'user_name': user.username,
        'num_stocks' : num_stocks,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'user_page.html', context=context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserStockList(generic.ListView):
    model = Stock
    context_object_name = "user_stock_list"
    template_name = "user_stock_list.html"

    def get_queryset(self):
        return self.request.user.profile.stocks.all()

    def get_context_data(self, **kwargs):
        context = super(UserStockList, self).get_context_data(**kwargs)
        context['form'] = NewStockForm()
        return context

    def post(self, request, *args, **kwargs):
        # Perform logic to add the new symbol
        tickerForm = NewStockForm(request.post)
        if tickerForm.is_valid():
            tickerForm.update()
            user = request.user

            # Update the list of user held stocks
            stock = Stock.objects.get(pk=tickerForm.ticker)

            # 1. If stock not part of list of user stocks, then add
            # 2. If stock is part of user stocks, then update with latest data
            found = False
            for userStock in user.profile.stocks:
                if userStock.ticker_symbol == stock.ticker_symbol:
                    userStock.refresh_from_db()
                    found = True
                    break

            if not found:
                user.profile.stocks.add(stock)

        # Render an updated page. Right now just keep the status quo

        # TODO: Add a success or failure method

        # TODO: Add a remove button

        return self.get(request=request, *args, **kwargs)
