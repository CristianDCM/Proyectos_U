import os
import random

def Crecer_Snake():
    global Comida
    Nueva_Cabeza = Cuerpo_Snake[0][0] + \
        Direction[0], Cuerpo_Snake[0][1] + Direction[1]
    Cuerpo_Snake.insert(0, Nueva_Cabeza)
    if not Comida:
        Cuerpo_Snake.pop(-1)
    Comida = False

def Mov():
    global Direction
    Controls = {"a": (-1, 0), "d": (1, 0), "w": (0, -1), "s": (0, 1)}
    Press = input("Presiona una tecla: (W, A ,S ,D) ")
    if Press == "w":
        Direction = Controls["w"]
    elif Press == "s":
        Direction = Controls["s"]
    elif Press == "a":
        Direction = Controls["a"]
    elif Press == "d":
        Direction = Controls["d"]
    elif Press == "q":
        exit()

def Colision_comida():
    global Comida, Posicion_comida
    if Cuerpo_Snake[0] == Posicion_comida:
        Posicion_comida = Colocar_comida()
        Comida = True

def Colocar_comida():
    Col = random.randint(1, W-2)
    Row = random.randint(1, H-2)
    while (Col, Row) in Cuerpo_Snake:
        Col = random.randint(1, W-2)
        Row = random.randint(1, H-2)
    return (Col, Row)

def Imprimir_tablero():
    for i in Tablero:
        if i in Cuerpo_Snake:
            print("■", end="")
        elif i == Posicion_comida:
            print("X", end="")
        elif i[1] in (0, H-1) or i[0] in (0, W-1):
            print("#", end="")
        else:
            print(" ", end="")
        if i[0] == W-1:
            print("")

def Game_Over():
    if Cuerpo_Snake[0][0] in (0, W-1) or Cuerpo_Snake[0][1] in (0, H-1):
        print("Game Over")
        exit()
    for i in Cuerpo_Snake[1:]:
        if Cuerpo_Snake[0] == i:
            print("Game Over")
            exit()

global W, H
W = 25
H = 15
Cuerpo_Snake = [(4, H//2), (3, H//2), (2, H//2)]
Tablero = [(Columna, Fila) for Fila in range(H) for Columna in range(W)]
Controls = {"a": (-1, 0), "d": (1, 0), "w": (0, -1), "s": (0, 1)}
Posicion_comida = Colocar_comida()
Comida = False

def Main():
    print(Tablero)
    while True:
        Imprimir_tablero()
        Mov()
        Crecer_Snake()
        Colision_comida()
        Game_Over()

if __name__ == "__main__":
    Main()