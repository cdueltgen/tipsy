import sqlite3
import datetime

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
    c = db.cursor()
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
    result = c.execute(query, (email, password, name))
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))
    return None

def new_task(db, title, user_id):
    c = db.cursor()
    now = datetime.datetime.now()
    query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
    result = c.execute(query, (title, now, user_id))
    db.commit()
    return result.lastrowid

