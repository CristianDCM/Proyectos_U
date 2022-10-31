import random
Snake = "■"
Apple = "★"

def Main(): 
    Crear_tablero()
    Pos_Snake_Random = Snake_Random(Snake) 
    Pos_Apple = Comida(Apple)
    Pos_Snake_Actual = []
    Pos_Snake_Anterior = []

    while True:
        Pos_Snake_Actual, Pos_Snake_Anterior = Mov(Pos_Snake_Random, Snake)
        Crecer(Pos_Snake_Anterior)
        Imprimir_tablero()
        print(Pos_Snake_Actual, Pos_Snake_Anterior)

        if Pos_Snake_Actual == Pos_Apple:
            Pos_Apple = Comida(Apple)

def Crecer(Pos_Snake_Anterior):
    Tablero[Pos_Snake_Anterior[0]][Pos_Snake_Anterior[1]] = " "
        
def Snake_Random(Snake):
    Pos_Snake_Actual = [random.randint(0, 9), random.randint(0, 9)]
    Tablero[Pos_Snake_Actual[0]][Pos_Snake_Actual[1]] = Snake
    return Pos_Snake_Actual

def Comida(Apple):
    Pos_Apple = [random.randint(0, 9), random.randint(0, 9)]
    Tablero[Pos_Apple[0]][Pos_Apple[1]] = Apple
    return Pos_Apple

def Mov(Pos_Snake_Actual, Snake):
    Press = input("¿Dónde quieres mover la culebrita? (W, A, S, D): ")
    Pos_Snake_Anterior = Pos_Snake_Actual[:]
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

    Tablero[Pos_Snake_Actual[0]][Pos_Snake_Actual[1]] = Snake

    return Pos_Snake_Actual, Pos_Snake_Anterior

def Imprimir_tablero():
    print("#" + " ─" * 10 + " #")
    for i in range(10):
        print("|", " ".join(Tablero[i]), "|")
    print("#" + " ─" * 10 + " #")

def Crear_tablero():
    global Tablero
    Tablero = []
    for i in range(10):
        Tablero.append([" "]*10)

if __name__ == "__main__":
    Main()
