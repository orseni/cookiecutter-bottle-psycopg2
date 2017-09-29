# -*- coding: utf-8 -*-
"""Main module."""
import os.path
from bottle import run

from services import *

def main():
    options = {'host': 'localhost', 'port': 8080, 'server': 'bjoern',
               'workers': 1, 'reload': False, 'debug': False}

    if os.path.isfile("config.json"):
        with open("config.json") as config_file:
            options = eval(''.join(config_file.readlines()))

    run(**options)


if __name__ == "__main__":
    main()
