import random 
from pytimedinput import timedInput  # pip install pytimedinput
import os  # pip install os-sys
import Desing
import Connection
import datetime
import time
import pandas as pd
import sqlalchemy as db 


def displayScoreTable():  # Muestra la tabla de puntuaciones
    connection = Connection.connect()
    df = pd.read_sql_table('pointstable', connection)
    print(df)

def createBoard():  # Crea el tablero
    global tablero
    tablero = []
    for i in range(H):
        tablero.append([" "] * W)


def printBoard():  # Imprime el tablero
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


def snakeGrowthMove():  # Mueve snake
    nuevaCabeza = [cuerpoSnake[0][0] + movimientoSnake[0],
                   cuerpoSnake[0][1] + movimientoSnake[1]]
    cuerpoSnake.insert(0, nuevaCabeza)
    if cuerpoSnake[0] != posicApple:
        cuerpoSnake.pop()


def isGameOver():  # Comprueba si el juego ha terminado
    # Si la cabeza de la culebrita toca los bordes
    if cuerpoSnake[0][0] == -1 or cuerpoSnake[0][0] == H or cuerpoSnake[0][1] == -1 or cuerpoSnake[0][1] == W:
        return True
    for i in cuerpoSnake[1:]:  # Si la cabeza de la culebrita toca su cuerpo
        if cuerpoSnake[0] == i:
            return True


def getControls():  # Obtiene los controles
    global movimientoSnake
    getControls = {"W": [-1, 0], "A": [0, -1], "S": [1, 0],
                   "D": [0, 1]}  # Arriba, Izquierda, Abajo, Derecha
    # Introduce una tecla y si no introduce nada, se mueve hacia la misma dirección
    press, _ = timedInput(
        "¿Dónde quieres mover la culebrita? (W, A, S, D): ", timeout=0.3)
    if press == "w" or press == "W":
        movimientoSnake = getControls["W"]
    elif press == "a" or press == "A":
        movimientoSnake = getControls["A"]
    elif press == "s" or press == "S":
        movimientoSnake = getControls["S"]
    elif press == "d" or press == "D":
        movimientoSnake = getControls["D"]
    else:
        if press == "":
            pass
        else:
            print("Introduce una tecla válida")


def generateFoodPosition():  # Genera la posición de la comida
    global posicApple
    posicApple = [random.randint(0, H - 1), random.randint(0, W - 1)]
    while posicApple in cuerpoSnake:
        posicApple = [random.randint(0, H - 1), random.randint(0, W - 1)]
    tablero[posicApple[0]][posicApple[1]] = "★"


# Inserta la información de la puntuación
def insertScoreInfo(nickname, score, time, datetime):
    try:
        #insertar en la base de datos los datos con sqlalchemy
        connection = Connection.connect()
        query = db.insert('pointstable').values(nickname=nickname, score=score, time=time, fecha=datetime)
        ResultProxy = connection.execute(query)
        return ResultProxy
    except Exception as e:
        print("Error: ", e)


def snakeGameMain():  # Función principal del juego
    print(Desing.menuPrincipal[0])
    print("1. Jugar \n2. Tabla de puntuaciones \n3. Salir")
    opc = input("Elige una opción: ")
    if opc == "1":
        nickname = input("Introduce tu nickname: ")
        createBoard()
        generateFoodPosition()
        startTime = time.time()
        while True:
            os.system("cls")
            printBoard()
            getControls()
            snakeGrowthMove()
            timeSeconds = int(time.time() - startTime)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if isGameOver():
                global cuerpoSnake, movimientoSnake
                score = (len(cuerpoSnake) - 3) * 10
                print(f"Score: {score}" + "\n" +
                      f"Time: {timeSeconds} seconds")
                insertScoreInfo(nickname, score, timeSeconds, date)
                cuerpoSnake = [[1, 5], [1, 6], [1, 7]]  # Reinicia posición
                movimientoSnake = [1, 0]  # Reinicia dirección
                snakeGameMain()
            if cuerpoSnake[0] == posicApple:
                generateFoodPosition()
    elif opc == "2":
        displayScoreTable()
    elif opc == "3":
        exit()
    else:
        print("Introduce una opción válida")
        snakeGameMain()


H = 10  # Alto
W = 10  # Ancho
cuerpoSnake = [[1, 5], [1, 6], [1, 7]]  # Cuerpo Snake(Cabeza, Cuerpo, Cola)
comida = False
movimientoSnake = [1, 0]

if __name__ == "__main__":
    snakeGameMain()
