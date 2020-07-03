from django.db import models

# Create your models here.
class Stock(models.Model):
    """
    Representation of a specific stock (from an exchange)
    """
    ticker_symbol = models.CharField(max_length=8, help_text="A company's ticker symbol", primary_key=True)
    company_name = models.CharField(max_length=40, help_text="The companies' name")
    price = models.DecimalField(help_text="The price of the stock", decimal_places=2, max_digits=8)
    daily_change = models.DecimalField(help_text="The daily change (in dollars) of the stock", decimal_places=2, max_digits=8)
    year_high = models.DecimalField(help_text="The high price of the stock during the year", decimal_places=2, max_digits=8)
    year_low = models.DecimalField(help_text="The low price of the stock during the year", decimal_places=2, max_digits=8)
    daily_percent = models.DecimalField(help_text="The daily percent change of the stock", decimal_places=2, max_digits=8)
    last_updated_date = models.DateField(help_text="The date when the stock information was last updated", auto_now=True)
    date_added = models.DateField(help_text="The date the stock was added to the database", auto_now_add=True)
    streak = models.IntegerField(help_text="Represents a streak of positive or negative earnings.")
    # TODO: Add a foreign key to the user_accounts database model
    # TODO: Add a field for current price when added
