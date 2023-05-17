import sqlite3 as sqli

db_connect = sqli.connect("hw21_db.sqlite")
cursor = db_connect.cursor()