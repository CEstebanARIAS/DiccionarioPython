import sqlite3

def connect():
    conn = sqlite3.connect('learnPython.db')
    return conn
