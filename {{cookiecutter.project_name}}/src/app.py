# -*- coding: utf-8 -*-
"""Main module."""
from os.path import dirname
import logging.config
import bottle
import pg_simple

from services import *

#logging.config.fileConfig("{}/{}".format(dirname(__file__), 'logging.ini'))
logging.config.fileConfig("logging.ini")

with open("database.conf") as config_file:
    pg_simple.config_pool(dsn=config_file.readlines()[0])

app = bottle.default_app()

if __name__ == "__main__":
    dev_options = {'host': '0.0.0.0', 'port': 8000,
                   'workers': 1, 'reload': True, 'debug': True}
    bottle.run(**dev_options)
