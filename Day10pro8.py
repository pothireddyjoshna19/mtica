import sqlite3 as lite
con = lite.connect('mtica.db')

cur=con.cursor()
cur.execute("SELECT * FROM cars")
rows=cur.fetchall()
for row in rows:
    print(row)
