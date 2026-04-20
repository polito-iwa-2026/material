import sqlite3

my_query = "INSERT INTO Users (name, surname, email, birthdate) VALUES (?, ?, ?, ?)"

conn = sqlite3.connect("example.db")

cursor = conn.cursor()

cursor.execute(my_query, ("Juan Pablo", "Saenz", "juan@test.com", "20-04-26"))

conn.commit()

cursor.close()

conn.close()