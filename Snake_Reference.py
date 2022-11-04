import random

def Crecer_Snake():  #Funcion para que el cuerpo de la serpiente crezca
    global Comida #Variable global para que la comida se agregue al cuerpo de la serpiente
    Nueva_Cabeza = Cuerpo_Snake[0][0] + Direction[0], Cuerpo_Snake[0][1] + Direction[1] #Nueva cabeza de la serpiente
    Cuerpo_Snake.insert(0, Nueva_Cabeza) #Inserta la nueva cabeza de la serpiente
    if not Comida:  #Si no hay comida, elimina el ultimo elemento de la serpiente #AQUI ES
        Cuerpo_Snake.pop(-1) #Elimina el ultimo elemento de la serpiente
    Comida = False #La comida se vuelve falsa para que la serpiente no crezca

def Mov():  #Funcion para mover la serpiente
    global Direction #Variable global para que la direccion de la serpiente se pueda cambiar
    Controls = {"a": (-1, 0), "d": (1, 0), "w": (0, -1), "s": (0, 1)} #Controles para mover la serpiente
    Press = input("Presiona una tecla: (W, A ,S ,D) ") #Pide al usuario que presione una tecla
    if Press == "w":    #Si presiona w, la serpiente se mueve hacia arriba
        Direction = Controls["w"] #La direccion de la serpiente es hacia arriba
    elif Press == "s":
        Direction = Controls["s"]
    elif Press == "a":
        Direction = Controls["a"]
    elif Press == "d":
        Direction = Controls["d"]

def Colision_comida():  #Funcion para que la serpiente coma la comida
    global Comida, Posicion_comida #Variable global para que la comida se agregue al cuerpo de la serpiente
    if Cuerpo_Snake[0] == Posicion_comida: #Si la cabeza de la serpiente esta en la posicion de la comida
        Posicion_comida = Colocar_comida() #La posicion de la comida se vuelve la nueva posicion de la comida
        

def Colocar_comida(): #Funcion para colocar la comida
    Col = random.randint(1, W-2) #Colocacion de la comida en el eje x
    Row = random.randint(1, H-2) #Colocacion de la comida en el eje y
    while (Col, Row) in Cuerpo_Snake: #Si la comida esta en el cuerpo de la serpiente
        Col = random.randint(1, W-2)    #La comida se vuelve a colocar en el eje x
        Row = random.randint(1, H-2)   #La comida se vuelve a colocar en el eje y
    return (Col, Row) #Retorna la posicion de la comida

def Imprimir_tablero(): #Funcion para imprimir el tablero
    for i in Tablero: #Para cada elemento en el tablero
        if i in Cuerpo_Snake: #Si el elemento esta en el cuerpo de la serpiente
            print("■", end="") #Imprime un ■
        elif i == Posicion_comida: #Si el elemento esta en la posicion de la comida
            print("X", end="") #Imprime una X
        elif i[1] in (0, H-1) or i[0] in (0, W-1): #Si el elemento esta en el borde del tablero
            print("#", end="") #Imprime un #
        else: #Si no esta en el cuerpo de la serpiente, en la posicion de la comida o en el borde del tablero
            print(" ", end="") #Imprime un espacio
        if i[0] == W-1: #Si el elemento esta en el borde del tablero
            print("") #Imprime un salto de linea

def Game_Over(): #Funcion para que el juego termine
    if Cuerpo_Snake[0][0] in (0, W-1) or Cuerpo_Snake[0][1] in (0, H-1): #Si la cabeza de la serpiente esta en el borde del tablero
        print("Game Over") #Imprime Game Over
        exit() #Termina el juego
    for i in Cuerpo_Snake[1:]: #Para cada elemento en el cuerpo de la serpiente
        if Cuerpo_Snake[0] == i: #Si la cabeza de la serpiente esta en el cuerpo de la serpiente
            print("Game Over") #Imprime Game Over
            exit() #Termina el juego
 
def Main(): #Funcion principal
    while True: #Ciclo infinito
        Imprimir_tablero() #Imprime el tablero
        Mov() #Mueve la serpiente
        Crecer_Snake() #Hace que el cuerpo de la serpiente crezca
        print(Posicion_comida) #Imprime la posicion de la comida

global W, H #Variables globales para el ancho y el alto del tablero
W = 25 #Ancho del tablero
H = 15 #Alto del tablero
Cuerpo_Snake = [(4, H//2), (3, H//2), (2, H//2)] #Cuerpo de la serpiente con una longitud de 3 elementos
Tablero = [(Columna, Fila) for Fila in range(H) for Columna in range(W)] #Tablero

Posicion_comida = Colocar_comida()  #Posicion de la comida
Comida = False #Comida falsa para que la serpiente no crezca

if __name__ == "__main__": #Si el archivo se esta ejecutando
    Main() #Ejecuta la funcion principal