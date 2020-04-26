from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('stocks/', TemplateView.as_view(template_name='stock_overview.html'), name='stock_overview')
]