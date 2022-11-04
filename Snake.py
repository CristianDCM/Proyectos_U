import random

def Crear_tablero():
    global Tablero
    Tablero = []
    for i in range(H):
        Tablero.append([" "] * W)

def Imprimir_tablero():
    for i in Cuerpo_Snake:
        if i == Cuerpo_Snake[0]:
            Tablero[i[0]][i[1]] = "■"
        else:
            Tablero[i[0]][i[1]] = "▪"

    print("#" + " ─" * H + " #")
    for i in range(10):
        print("|", " ".join(Tablero[i]), "|")
    print("#" + " ─" * H + " #")

def Mov():
    Press = input("¿Dónde quieres mover la culebrita? (W, A, S, D): ")
    if Press == "w" or Press == "W":
        Cuerpo_Snake.insert(0, [Cuerpo_Snake[0][0] - 1, Cuerpo_Snake[0][1]])
    elif Press == "a" or Press == "A":
        Cuerpo_Snake.insert(0, [Cuerpo_Snake[0][0], Cuerpo_Snake[0][1] - 1])
    elif Press == "s" or Press == "S":
        Cuerpo_Snake.insert(0, [Cuerpo_Snake[0][0] + 1, Cuerpo_Snake[0][1]])
    elif Press == "d" or Press == "D":
        Cuerpo_Snake.insert(0, [Cuerpo_Snake[0][0], Cuerpo_Snake[0][1] + 1])

def Comida():
    Pos_Apple = [random.randint(0, 9), random.randint(0, 9)]
    Tablero[Pos_Apple[0]][Pos_Apple[1]] = "★"
    return Pos_Apple

def Main(): 
    Crear_tablero()
    Pos_Apple = Comida()
    while True:
        Imprimir_tablero()
        Mov()
        if Cuerpo_Snake[0] == Pos_Apple:
            Pos_Apple = Comida()

Cuerpo_Snake = [[1,1], [1,2], [1,3]]
W = 10
H = 10

if __name__ == "__main__":
    Main()