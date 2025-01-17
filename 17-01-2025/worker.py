import mysql.connector as c

mydb = c.connect(
host="localhost",
user="root",
password="1234",
database="test"
)

if mydb.is_connected():
print("Successfully connected to the database!")
else:
print("Failed to connect.")

mycursor = mydb.cursor()

mycursor.execute('''
CREATE TABLE IF NOT EXISTS workers (
student_id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
score INT,
city VARCHAR(100)
)
''')

mycursor.execute("INSERT INTO workers (student_id, name, score, city) VALUES (1, 'John Doe', 85, 'Hyderabad')")
mycursor.execute("INSERT INTO workers (student_id, name, score, city) VALUES (2, 'Jane Doe', 65, 'Mumbai')")
mycursor.execute("INSERT INTO workers (student_id, name, score, city) VALUES (3, 'ABC', 75, 'Bangalore')")
mycursor.execute("INSERT INTO workers (student_id, name, score, city) VALUES (4, 'XYZ', 75, 'Bangalore')")

mycursor.execute("DELETE FROM workers WHERE student_id = 4")

mycursor.execute("UPDATE workers SET name = 'John Smith', score = 90, city = 'Hyderabad' WHERE student_id = 1")

mycursor.execute("SELECT * FROM workers")
for row in mycursor.fetchall():
print(row)

mycursor.execute("SELECT * FROM workers ORDER BY name ASC")
for row in mycursor.fetchall():
print(row)

mycursor.execute("SELECT * FROM workers WHERE score BETWEEN 70 AND 90")
for row in mycursor.fetchall():
print(row)

mycursor.execute("SELECT * FROM workers WHERE city = 'Hyderabad'")
for row in mycursor.fetchall():
print(row)

mydb.commit()

mycursor.close()
mydb.close()