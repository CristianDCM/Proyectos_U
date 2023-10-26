import mysql.connector

def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gamesnake",
    )
        return connection
    except mysql.connector.Error as err:
        print(err)
