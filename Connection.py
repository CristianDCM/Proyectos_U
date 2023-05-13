import mysql.connector

def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port = 3307,
            user = "root",
            password = "usbw",
            database = "gamesnake"
        )
    except mysql.connector.Error as e:
        print("Error en la conexión", e)
        connection = None
    return connection

def insert(connection, nickname, score, time, fecha):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO pointstable (nickname, score, time, datetime) VALUES (%s, %s, %s, %s)"
        val = (nickname, score, time, fecha)
        cursor.execute(sql, val)
        connection.commit()
    except mysql.connector.Error as e:
        print("Error al insertar datos", e)