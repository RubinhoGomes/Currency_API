import secrets
import json
from os.path import exists

def check_file():
    return exists('./config')

def create_config(SQLALCHEMY_DATABASE_URL=None, CURRENCY='EUR', CURRENCY_SYMBOL=None):
    class Config:
        def __init__(self):
            self.SECRET_KEY = secrets.token_hex(32)
            self.SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL
            self.CURRENCY = CURRENCY
            self.CURRENCY_SYMBOL = CURRENCY_SYMBOL
            self.VALIDATION = False

    # Create an instance of the Config class
    config_instance = Config()

    # Serialize the instance to JSON
    return config_instance.__dict__

def get_config():
    if not check_file():
        config = create_config()  # Create config if file doesn't exist
        with open('./config', 'w') as fp:
            for key, value in config.items():
                fp.write(f'{key}={value}\n')
        return config

    try:
        config = {}
        with open('./config', 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split('=')
                config[key] = value
        return config
    except FileNotFoundError:
        return None

def set_config(config_data):
    with open('./config', 'w') as file:
        for key, value in config_data.items():
            file.write(f'{key}={value}\n')


## TODO: Implement the update_validation function
## This shit is not working ... so resolve it
def update_validation():
    config = get_config()
    config['VALIDATION'] = True
    set_config(config)

test = create_config()
set_config(test)
print(get_config())
