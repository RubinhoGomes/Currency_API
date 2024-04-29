# @Author: Rubinho
# @Date: 2021-01-31
# @Description: This script is a simple currency converter using webscrapping to get the rates from x-rates.com

# @Brief: All imports
from enum import Enum
import requests
import json
from bs4 import BeautifulSoup

# @Brief: Enum class to represent the currency
class Currency(Enum):
    USD = 'USD'
    EUR = 'EUR'
    JPY = 'JPY'
    GBP = 'GBP'
    AUD = 'AUD'
    CAD = 'CAD'
    CHF = 'CHF'

# @Brief: Class Calculator to represent the object that will be returned as JSON
class Calculator:
    #@Note: Constructor for Calculator class, this constructor will receive the value, the currency from and the currency
    def __init__(self, value, from_currency, to_currency):
        self.value = value
        self.from_currency = from_currency
        self.to_currency = to_currency
    
    #@Note: Method to return the object as JSON
    def to_json(self):
        return {
            'value': self.value,
            'from_currency': self.from_currency,
            'to_currency': self.to_currency
        }

# @Brief: Class CurrencyConverter to convert the currency and get the rates
class CurrencyConverter:
    
    #@Brief: Method to calculate the currency
    @staticmethod
    def calculate(amount, currency_from, currency_to):
        #@Note: URL to fetch the data 
        URL_calculate = f'https://www.x-rates.com/calculator/?from={currency_from}&to={currency_to}&amount={amount}'
        #@Note: Get the page content
        page = requests.get(URL_calculate)
        #@Note: Parse the page content
        soup = BeautifulSoup(page.content, 'html.parser')

        #@Note: Get the value from the page
        value = soup.find_all('span', class_='ccOutputRslt')[0].get_text()
        #@Note: Remove the currency from the value to get only the number
        value = value.replace(currency_to, '')

        #@Note: Create the object Calculator
        calc = Calculator(value, currency_from, currency_to)
        #@Note: Return the object as JSON
        return json.dumps(calc.to_json())

    #@Brief: Method to get the rates using the top 10 currencies
    @staticmethod
    def get_rates(currency, amount):
        #@Note: URL to fetch the data
        URL_get = f'https://www.x-rates.com/table/?from={currency}&amount={amount}'
        #@Note: Get the page content
        page = requests.get(URL_get)
        #@Note: Parse the page content
        soup = BeautifulSoup(page.content, 'html.parser')
        #@Note: Get the table content of the top 10 currencies
        rows = soup.find('table', class_='ratesTable').find('tbody').find_all('tr')
        
        #@Note: Create a dictionary to store the data, and the variables needed
        values = []
        json_dict = {}
        i = 0
        
        #@Note: Iterate over the rows to get the data
        for row in rows:
            values = row.get_text().split('\n')
            #@Note: Store the data in the dictionary to return as JSON
            json_dict[i] = {
                'currency': values[1],
                'rate': values[2],
                'inverse_rate': values[3]
            }
            i += 1
        #@Note: Return the dictionary as JSON
        return json.dumps(json_dict)

# Example usage
# result = CurrencyConverter.calculate(100, Currency.USD.name, Currency.EUR.name)
# print(result)
