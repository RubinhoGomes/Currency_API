## @Brief: This is the init file, it used to import the functions from the setup_config.py file

from .setup_config import create_config, check_file

if check_file() == False:
    create_config()
else:
    pass

