import random

def Crear_tablero():
    global Tablero 
    Tablero = []
    for i in range(H):
        Tablero.append([" "] * W)

def Imprimir_tablero():
    for i in Cuerpo_Snake: #Añadir Snake al tablero
        if i == Cuerpo_Snake[0]:
            Tablero[i[0]][i[1]] = "■"
        else:
            Tablero[i[0]][i[1]] = "▪"

    print("#" + " ─" * W + " #") #Marco
    for i in Tablero:
        print("|", end = " ")
        for j in i:
            print(j, end = " ") 
        print("|")
    print("#" + " ─" * W + " #")

def Crecimiento_Mov():
    Nueva_Cabeza = [Cuerpo_Snake[0][0] + Movimiento_Snake[0], Cuerpo_Snake[0][1] + Movimiento_Snake[1]]
    Cuerpo_Snake.insert(0, Nueva_Cabeza)

def Controles():
    global Movimiento_Snake
    Press = input("¿Dónde quieres mover la culebrita? (W, A, S, D): ")
    Controles = {"W": [-1, 0], "A": [0, -1], "S": [1, 0], "D": [0, 1]} #Arriba, Izquierda, Abajo, Derecha
    if Press == "w" or Press == "W":
        Movimiento_Snake = Controles["W"]
    elif Press == "a" or Press == "A":
        Movimiento_Snake = Controles["A"]
    elif Press == "s" or Press == "S":
        Movimiento_Snake = Controles["S"]
    elif Press == "d" or Press == "D":
        Movimiento_Snake = Controles["D"]

def Posicion_Comida():
    global Pos_Apple
    Pos_Apple = [random.randint(0, 9), random.randint(0, 9)]
    Tablero[Pos_Apple[0]][Pos_Apple[1]] = "★"

def Main():
    Crear_tablero()
    Posicion_Comida()
    while True:
        Imprimir_tablero()
        Controles()
        Crecimiento_Mov()
        if Cuerpo_Snake[0] == Pos_Apple:
            Posicion_Comida()

Cuerpo_Snake = [[1,1], [1,2], [1,3]] #Cuerpo Snake(Cabeza, Cuerpo, Cola)
W = 40
H = 10

if __name__ == "__main__":
    Main()