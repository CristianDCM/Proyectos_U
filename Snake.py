import random

def Crear_tablero():
    global Tablero
    Tablero = []
    for i in range(H):
        Tablero.append([" "] * W)

def Imprimir_tablero():
    print("#" + " ─" * H + " #")
    for i in range(10):
        print("|", " ".join(Tablero[i]), "|")
    print("#" + " ─" * H + " #")

def Mov():
    Press = input("¿Dónde quieres mover la culebrita? (W, A, S, D): ")
    if Press == "w" or Press == "W":
        if Pos_Snake_Actual[0] == 0:
            print("No puedes salirte del Tablero")
        else:
            Pos_Snake_Actual[0] -= 1
    elif Press == "a" or Press == "A":
        if Pos_Snake_Actual[1] == 0:
            print("No puedes salirte del Tablero")
        else:
            Pos_Snake_Actual[1] -= 1
    elif Press == "s" or Press == "S":
        if Pos_Snake_Actual[0] == 9:
            print("No puedes salirte del Tablero")
        else:   
            Pos_Snake_Actual[0] += 1
    elif Press == "d" or Press == "D":
        if Pos_Snake_Actual[1] == 9:
            print("No puedes salirte del Tablero")
        else:
            Pos_Snake_Actual[1] += 1
    Tablero[Pos_Snake_Actual[0]][Pos_Snake_Actual[1]] = "■"

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
        if Pos_Snake_Actual == Pos_Apple:
            Pos_Apple = Comida()

Pos_Snake_Actual = [random.randint(0, 9), random.randint(0, 9)]
W = 10
H = 10

if __name__ == "__main__":
    Main()