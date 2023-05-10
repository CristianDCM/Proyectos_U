import cx_Oracle as cx

def get_connection():
    user , password  = 'system' , '12345'  
    try :
        con = cx.connect(user,password,'localhost:1521/xe')
        print("Conexión exitosa")
        return con
    except cx.Error as error:
        print("Error al conectar a la base de datos ",error)