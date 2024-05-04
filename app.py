from webscrapping import currency_webscrapping
from config import create_config, update_validation
from flask import Flask, request


app = Flask(__name__)

@app.route('/activate')
def activation():
    secret_key = request.args.post('SECRET_KEY')
    validation = request.args.post('VALIDATION')
    if(validation == False):
        config.update_validation()
        with open('./logs.txt') as file:
            file.write(f'{secret_key}\n')

    return 'Your access key was activated'

@app.route('/calculate')
def calculate():
    amount = request.args.get('amount')
    from_currency = request.args.get('from_currency')
    to_currency = request.args.get('to_currency')   
    
    result = currency_webscrapping.CurrencyConverter.calculate(amount, from_currency, to_currency)
    
    return result

@app.route('/get/rates')
def get_rates():
    currency = request.args.get('currency')
    amount = request.args.get('amount')

    result = currency_webscrapping.CurrencyConverter.get_rates(currency, amount)
    
    return result


