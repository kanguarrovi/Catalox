import sqlite3

conn = sqlite3.connect('catalox.db')
print("Opened database successfully")

conn.execute('CREATE TABLE Vinyl(id INTEGER PRIMARY KEY AUTOINCREMENT,image VARCHAR(255) NULL,artist VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,price REAL NOT NULL,saved BOOLEAN DEFAULT 0,sold BOOLEAN DEFAULT 0,info TEXT DEFAULT "");')
print("Table created successfully")
conn.close()
