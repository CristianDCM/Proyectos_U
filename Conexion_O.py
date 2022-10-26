
import cx_Oracle
import tkinter as tk

def Conexion_O():
    try:
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        print("Conexion exitosa")
    except cx_Oracle.DatabaseError as e:
        print("Error al conectar", e)
    return con

def Desconectar_O(con):
    try:
        con.close()
        print("Desconexion exitosa")
    except cx_Oracle.DatabaseError as e:
        print("Error al desconectar", e)

#crear ventana principal
ventana = tk.Tk()
ventana.title("Conexion Oracle")
ventana.geometry("400x400")

boton = tk.Button(ventana, text="Conectar", command=Conexion_O)
boton.pack()
#boton desconectar
boton2 = tk.Button(ventana, text="Desconectar", command=Desconectar_O(Conexion_O()))
boton2.pack()
ventana.mainloop()
