import sqlite3 as sql
from homework21.hw21_sqlite import get_queries

db_connection = sql.connect("db/hw_bookstore.sqlite")
cursor = db_connection.cursor()


if __name__ == "__main__":
    queries = get_queries("task1.sql")
    for q in queries:
        cursor.execute(q)
