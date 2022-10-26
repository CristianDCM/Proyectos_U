import cx_Oracle
#formato de conexion
con = cx_Oracle.connect("usuario/contraseña@ip:puerto/sid")
#ejecutar consulta
cursor = con.cursor()
cursor.execute("select * from tabla")
#recorrer consulta
for row in cursor:
    print(row)