import sqlite3
conn = sqlite3.connect("example.db")
print(conn.table)