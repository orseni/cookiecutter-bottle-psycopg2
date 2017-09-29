# -*- coding: utf-8 -*-
"""
    User service example
"""
from bottle import get

@get("/users/<id>")
def load(id):
    """ Load user from id """
    return {"id": int(id)}

@get("/users")
def query():
    """ Load all users """
    return {"id": "xxxx"}
