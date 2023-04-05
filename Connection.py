from ast import Return
import mysql.connector

mydb = mysql.connector.connect(

host = "localhost",
user = "root",
password = "",
database = "mydatabase"

)

mycursor = mydb.cursor()

for x in mycursor:
  print(x)

mycursor.execute("CREATE TABLE users (name VARCHAR(255), lastname VARCHAR(255))")

sql = "INSERT INTO customers (firstname, lastname) VALUES (%s, %s)"
val =[
("John", "Highway"),
("Iliya", "Khoshrouy"),
("Mohammad", "Roohbakhsh"),
("Shayan", "Bahrami"),
("Moeid", "Mogharabi"),
("Bill","%g")
] 

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Done!")
