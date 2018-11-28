import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="runoob"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchone()

print(myresult)