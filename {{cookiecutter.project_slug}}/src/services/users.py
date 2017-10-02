# -*- coding: utf-8 -*-
"""
    User service example
"""
import pg_simple
from bottle import get, put, request.params

@get("/users/<id>")
def load(id):
    """ Load user from id """
    with pg_simple.PgSimple() as db:
        user = db.fetchone('users',
                           fields=['id', 'name'],
                           where=('id = %s', [id]))
        return user


@get("/users")
def query():
    """ Load all users """
    with pg_simple.PgSimple() as db:
        users = db.fetchall('users',
                            fields=['id', 'name'],
                            order=['id', 'ASC'])
        return {"content": users}


@put("/users")
def insert():
    print(request.params.getall("param"))
    # """ Insert a user """
    # with pg_simple.PgSimple() as db:
    #     users = db.insert('users',
    #                       data=request.params)
    #     return {"content": users}
