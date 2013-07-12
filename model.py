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
    query = """INSERT INTO Tasks(title, created_at, user_id) VALUES (?, ?, ?)"""
    result = c.execute(query, (title, now, user_id))
    db.commit()
    return result.lastrowid

def get_user(db, user_id):
    c = db.cursor()
    query = """SELECT * from Users WHERE id=?"""
    c.execute(query, (user_id,))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))
    return None

def complete_task(db, task_id):
    c = db.cursor()
    now = datetime.datetime.now()
    query = """UPDATE Tasks SET completed_at=? WHERE id=?"""
    result = c.execute(query, (now, task_id))
    db.commit()
    return

def get_tasks(db, user_id):
    c = db.cursor()
    query = """SELECT * from Tasks WHERE user_id=?"""
    c.execute(query, (user_id,))
    return c.fetchall()

def get_task(db, task_id):
    c = db.cursor()
    query = """SELECT * from Tasks WHERE id=?"""
    c.execute(query, (task_id,))
    result = c.fetchone()
    if result:
        fields = ["id", "title", "created_at", "completed_at", "user_id"]
        return dict(zip(fields, result))
    return None
