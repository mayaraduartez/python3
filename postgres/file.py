import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="postgres", password="postgres", database='python')

mycursor = mydb.cursor()
sql = "INSERT INTO clientes (nome, idade, email) VALUES (%s, %s, %s)"
val = [
    ("Mayara", 19, "mayara@gmail.com"),
    ("Mayara", 19, "mayara@gmail.com"),
    ("Mayara", 19, "mayara@gmail.com"),
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "Registros inseridos!")