import sqlalchemy as db


def connect():
    try:
        engine = db.create_engine('mysql+mysqlconnector://root:usbw@localhost:3307/gamesnake')
        connection = engine.connect()
        return connection
    except db.exc.SQLAlchemyError as e:
        print("Error al conectar con la base de datos", e)
    

def insert(connection, nickname, score, time, fecha):
    try:
        query = db.insert('pointstable').values(nickname=nickname, score=score, time=time, fecha=fecha)
        ResultProxy = connection.execute(query)
        return ResultProxy
    except Exception as e:
        print("Error: ", e)