from webscrapping import currency_webscrapping
from flask import Flask, request


app = Flask(__name__)


@app.route('/calculate')
def calculate():
    amount = request.args.get('amount')
    from_currency = request.args.get('from_currency')
    to_currency = request.args.get('to_currency')   
    
    result = currency_webscrapping.CurrencyConverter.calculate(amount, from_currency, to_currency)
    
    return result

@app.route('/get/currency')
def get_currency():
    return currency_webscrapping.Currency.USD.name  
