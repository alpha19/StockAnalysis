# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import User
from stock_management.models import Stock

from django.shortcuts import render

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
        #checked_objects.definitions.all()
        return self.request.user.profile.stocks.all()
