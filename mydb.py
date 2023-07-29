import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
)
#creating cursor object
cursorObject = dataBase.cursor()

#creating a datbase
cursorObject.execute("CREATE DATABASE pscom")

print("All done")