from enum import Enum
import requests
import json
from bs4 import BeautifulSoup

class Currency(Enum):
    USD = 'USD'
    EUR = 'EUR'
    JPY = 'JPY'
    GBP = 'GBP'
    AUD = 'AUD'
    CAD = 'CAD'
    CHF = 'CHF'

class Calculator:
    def __init__(self, value, from_currency, to_currency):
        self.value = value
        self.from_currency = from_currency
        self.to_currency = to_currency

    def to_json(self):
        return {
            'value': self.value,
            'from_currency': self.from_currency,
            'to_currency': self.to_currency
        }

class CurrencyConverter:
    @staticmethod
    def calculate(amount, currency_from, currency_to):

        URL = f'https://www.x-rates.com/calculator/?from={currency_from}&to={currency_to}&amount={amount}'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        value = soup.find_all('span', class_='ccOutputRslt')[0].get_text()
        value = value.replace(currency_to, '')

        calc = Calculator(value, currency_from, currency_to)
        return json.dumps(calc.to_json())


# Example usage
result = CurrencyConverter.calculate(100, Currency.USD.name, Currency.EUR.name)
print(result)

