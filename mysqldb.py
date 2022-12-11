import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="harish",
  password="test123",
  database="test1"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM userdetails")

myresult = mycursor.fetchall()

for x in myresult:
  print(f"Row from db {x}")