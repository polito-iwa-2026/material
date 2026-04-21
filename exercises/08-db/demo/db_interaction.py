import sqlite3

my_insert_query = "INSERT INTO Users (name, surname, email, birthdate) VALUES (?, ?, ?, ?)"

my_select_query = "SELECT * FROM Users WHERE Users.id = ?"

conn = sqlite3.connect("example.db")

cursor = conn.cursor()

cursor.execute(my_select_query, (1,))

rows = cursor.fetchone()

for row in rows:    
  print(row)

conn.commit()

cursor.close()

conn.close()