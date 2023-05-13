import random
from pytimedinput import timedInput  # pip install pytimedinput
import os  # pip install os-sys
import Desing
import Connection
import datetime
import mysql.connector
import time
import pandas as pd
def tableScore():
    s = pd.read_sql_query("SELECT * FROM pointstable", Connection.connect())
    s.columns = ['Nombre', 'Puntuación', 'Tiempo', 'Fecha']
    print(s)

def creartablero():
    global tablero
    tablero = []
    for i in range(H):
        tablero.append([" "] * W)

def imprimirTablero():
    for i in range(H):  # Recorre las filas
        for j in range(W):  # Recorre las columnas
            if [i, j] in cuerpoSnake:  # Si la posición está en la lista del cuerpo de snake
                if [i, j] == cuerpoSnake[0]:  # Si la posición es la cabeza de snake
                    tablero[i][j] = "◉"  # Pone la cabeza de snake
                else:
                    tablero[i][j] = "●"
            else:
                if tablero[i][j] != "★":
                    tablero[i][j] = " "

    print("╔" + "══" * W + "═╗")  # Borde superior
    for i in tablero:
        print("║", end=" ")  # Borde izquierdo
        for j in i:
            print(j, end=" ")  # Cuerpo del tablero
        print("║")  # Borde derecho
    print("╚" + "══" * W + "═╝")  # Borde inferior

def crecimientoMov():
    nuevaCabeza = [cuerpoSnake[0][0] + movimientoSnake[0],
                   cuerpoSnake[0][1] + movimientoSnake[1]]
    cuerpoSnake.insert(0, nuevaCabeza)
    if cuerpoSnake[0] != posicApple:
        cuerpoSnake.pop()

def gameOver():
    # Si la cabeza de la culebrita toca los bordes
    if cuerpoSnake[0][0] == -1 or cuerpoSnake[0][0] == H or cuerpoSnake[0][1] == -1 or cuerpoSnake[0][1] == W:
        return True
    for i in cuerpoSnake[1:]:  # Si la cabeza de la culebrita toca su cuerpo
        if cuerpoSnake[0] == i:
            return True

def controles():
    global movimientoSnake
    controles = {"W": [-1, 0], "A": [0, -1], "S": [1, 0],
                 "D": [0, 1]}  # Arriba, Izquierda, Abajo, Derecha
    # Introduce una tecla y si no introduce nada, se mueve hacia la misma dirección
    press, _ = timedInput(
        "¿Dónde quieres mover la culebrita? (W, A, S, D): ", timeout=0.3)
    if press == "w" or press == "W":
        movimientoSnake = controles["W"]
    elif press == "a" or press == "A":
        movimientoSnake = controles["A"]
    elif press == "s" or press == "S":
        movimientoSnake = controles["S"]
    elif press == "d" or press == "D":
        movimientoSnake = controles["D"]
    else:
        if press == "":
            pass
        else:
            print("Introduce una tecla válida")

def posiccomida():
    global posicApple
    posicApple = [random.randint(0, H - 1), random.randint(0, W - 1)]
    while posicApple in cuerpoSnake:
        posicApple = [random.randint(0, H - 1), random.randint(0, W - 1)]
    tablero[posicApple[0]][posicApple[1]] = "★"

def insercionInfo(nickname, score, time, datetime):
    try:
        Connection.insert(Connection.connect(), nickname,
                          score, time, datetime)
    except mysql.connector.Error as e:
        print("Error al insertar datos", e)

def main():
    print(Desing.menuPrincipal[0])  # Imprime el menú principal
    print("1. Jugar \n2. Tabla de puntuaciones \n3. Salir")
    opc = input("Elige una opción: ")
    if opc == "1":
        nickname = input("Introduce tu nickname: ")
        creartablero()
        posiccomida()
        startTime = time.time()
        while True:
            os.system("cls")
            imprimirTablero()
            controles()
            crecimientoMov()
            timeSeconds = int(time.time() - startTime)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if gameOver():
                print(timeSeconds)
                insercionInfo(nickname, score, timeSeconds, date)
                print("Game Over")
                global cuerpoSnake, movimientoSnake
                cuerpoSnake = [[1, 5], [1, 6], [1, 7]]  # Reinicia posición
                movimientoSnake = [1, 0]  # Reinicia dirección
                main()
            if cuerpoSnake[0] == posicApple:
                posiccomida()
            score = len(cuerpoSnake) - 2
            print("Score: ", score)
    elif opc == "2":
        tableScore()
    elif opc == "3":
        exit()
    else:
        print("Introduce una opción válida")
        main()

H = 10  # Alto
W = 10  # Ancho
cuerpoSnake = [[1, 5], [1, 6], [1, 7]]  # Cuerpo Snake(Cabeza, Cuerpo, Cola)
comida = False
movimientoSnake = [1, 0]

if __name__ == "__main__":
    main()