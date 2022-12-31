import sqlite3 as lite
con = lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute('''CREATE TABLE  cars(Id INT,Name TEXT,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO cars VALUES(1,'Audi',54678)")
cur.execute("INSERT INTO cars VALUES(2,'Tata',54906)")

cur.execute("INSERT INTO cars VALUES(3,'skoda',54072)")
cur.execute("INSERT INTO cars VALUES(4,'volvo',54006)")
cur.execute("INSERT INTO cars VALUES(5,'bentley',58678)")
cur.execute("INSERT INTO cars VALUES(6,'citroen',54956)")
cur.execute("INSERT INTO cars VALUES(7,'hummer',546128)")
cur.execute("INSERT INTO cars VALUES(8,'volkwagen',549456)")

con.commit()
print("values in table car inserted.")
