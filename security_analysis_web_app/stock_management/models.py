from django.db import models

# Create your models here.
class Stock(models.Model):
    """
    Representation of a specific stock (from an exchange)
    """
    ticker_symbol = models.CharField(max_length=8, help_text="A company's ticker symbol", primary_key=True)
    company_name = models.CharField(max_length=40, help_text="The companies' name")
    price = models.IntegerField(help_text="The price of the stock")
    daily_change = models.IntegerField(help_text="The daily change (in dollars) of the stock")
    year_high = models.IntegerField(help_text="The high price of the stock during the year")
    year_low = models.IntegerField(help_text="The low price of the stock during the year")
    daily_percent = models.IntegerField(help_text="The daily percent change of the stock")
    last_updated_date = models.DateField(help_text="The date when the stock information was last updated", auto_now=True)
    date_added = models.DateField(help_text="The date the stock was added to the database", auto_now_add=True)
    streak = models.IntegerField(help_text="Represents a streak of positive or negative earnings.")
    # TODO: Add a foreign key to the user_accounts database model
