import random

def Crear_tablero():
    global Tablero
    Tablero = []
    for i in range(H):
        Tablero.append([" "] * W)

def Imprimir_tablero():
    for i in range(H):
        for j in range(W):
            if [i, j] in Cuerpo_Snake:
                if [i, j] == Cuerpo_Snake[0]:
                    Tablero[i][j] = "◉"
                else:
                    Tablero[i][j] = "●"
            else:
                if Tablero[i][j] != "★":
                    Tablero[i][j] = " "

    print("╔" + "══" * W + "═╗") # Borde superior
    for i in Tablero:
        print("║", end=" ") # Borde izquierdo
        for j in i:
            print(j, end=" ") # Cuerpo del tablero
        print("║") # Borde derecho
    print("╚" + "══" * W + "═╝") # Borde inferior

def Crecimiento_Mov():
    Nueva_Cabeza = [Cuerpo_Snake[0][0] + Movimiento_Snake[0], Cuerpo_Snake[0][1] + Movimiento_Snake[1]]
    Cuerpo_Snake.insert(0, Nueva_Cabeza)
    if Cuerpo_Snake[0] != Pos_Apple:
        Cuerpo_Snake.pop()

def Game_Over():
    if Cuerpo_Snake[0][0] == -1 or Cuerpo_Snake[0][0] == H or Cuerpo_Snake[0][1] == -1 or Cuerpo_Snake[0][1] == W: # Si la cabeza de la culebrita toca los bordes
        return True 
    for i in Cuerpo_Snake[1:]: # Si la cabeza de la culebrita toca su cuerpo 
        if Cuerpo_Snake[0] == i:
            return True

def Controles():
    global Movimiento_Snake
    Controles = {"W": [-1, 0], "A": [0, -1], "S": [1, 0], "D": [0, 1]}  # Arriba, Izquierda, Abajo, Derecha
    Press = input("¿Dónde quieres mover la culebrita? (W, A, S, D): ")
    if Press == "w" or Press == "W":
        Movimiento_Snake = Controles["W"]
    elif Press == "a" or Press == "A":
        Movimiento_Snake = Controles["A"]
    elif Press == "s" or Press == "S":
        Movimiento_Snake = Controles["S"]
    elif Press == "d" or Press == "D":
        Movimiento_Snake = Controles["D"]
    else:
        if Press == "":
            pass
        else:
            print("Introduce una tecla válida")

def Posicion_Comida():
    global Pos_Apple
    Pos_Apple = [random.randint(0, H - 1), random.randint(0, W - 1)]
    while Pos_Apple in Cuerpo_Snake:
        Pos_Apple = [random.randint(0, H - 1), random.randint(0, W - 1)]
    Tablero[Pos_Apple[0]][Pos_Apple[1]] = "★"

def Main():
    Crear_tablero()
    Posicion_Comida()
    while True:
        Imprimir_tablero()
        Controles()
        Crecimiento_Mov()
        if Game_Over():
            print("Game Over")
            break
        if Cuerpo_Snake[0] == Pos_Apple:
            Posicion_Comida()
        print("Score: ", len(Cuerpo_Snake) - 2)

H = 10  # Alto
W = 10  # Ancho
Cuerpo_Snake = [[1, 5], [1, 6], [1, 7]]  # Cuerpo Snake(Cabeza, Cuerpo, Cola)
Comida = False
Movimiento_Snake=[0, 1]

if __name__ == "__main__":
    Main()