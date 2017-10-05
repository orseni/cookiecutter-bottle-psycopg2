# -*- coding: utf-8 -*-
"""Main module."""
import logging.config
import bottle
import pg_simple

from services import *

logging.config.fileConfig('logging.ini')

with open("database.conf") as config_file:
    pg_simple.config_pool(dsn=config_file.readlines()[0])

app = bottle.default_app()


if __name__ == "__main__":
    dev_options = {'host': 'localhost', 'port': 8000, 'server': 'gunicorn',
                   'workers': 1, 'reload': True, 'debug': True}
    bottle.run(**dev_options)
