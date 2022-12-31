import sqlite3 as lite
con = lite.connect('mtica.db')
cur=con.cursor()
cur.execute('''
UPDATE  cars SET Name='joshna' WHERE id=8
''')
con.commit()
con.close()
print("Data UPDATED")
