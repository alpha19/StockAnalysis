# accounts/urls.py
from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.UserStockList.as_view(), name='user_stock_list')
]