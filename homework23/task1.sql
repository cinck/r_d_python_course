CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT,
last_name TEXT,
age INTEGER);

CREATE TABLE IF NOT EXISTS publishing_houses
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
rating INTEGER DEFAULT 5);

CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
year INTEGER,
price REAL,
publishing_house_id INTEGER NOT NULL,
FOREIGN KEY (publishing_house_id) REFERENCES publishing_houses(id)
);

CREATE TABLE IF NOT EXISTS purchases
(id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
book_id INTEGER NOT NULL,
date TEXT DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (book_id) REFERENCES books(id)
);