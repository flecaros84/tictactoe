def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------+-------+-------+")
    print("|       |       |       |")  
    print(f"|   {board[0][0]}\t|   {board[0][1]}\t|   {board[0][2]}\t|")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")  
    print(f"|   {board[1][0]}\t|   {board[1][1]}\t|   {board[1][2]}\t|")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")  
    print(f"|   {board[2][0]}\t|   {board[2][1]}\t|   {board[2][2]}\t|")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            jugada = int(input("Ingrese su movimiento:"))
        except ValueError:
            print("Jugada Invalida. Debe ingresar un entero entre 1 y 9.")
        else:
            if jugada <= 0 or jugada > 9:
                print("Jugada Invalida. Debe ingresar un entero entre 1 y 9.")
            elif jugada <= 3:
                if (0,jugada-1) in make_list_of_free_fields(board):
                    board[0][jugada-1] = "O"
                    return
                else:
                    print("Jugada Invalida. Espacio Ocupado")
            elif jugada <=6:
                if (1,jugada-4) in make_list_of_free_fields(board):
                    board[1][jugada-4] = "O"
                    return
                else:
                    print("Jugada Invalida. Espacio Ocupado")
            else: 
                if (2,jugada-7) in make_list_of_free_fields(board):    
                    board[2][jugada-7] = "O"
                    return
                else:
                    print("Jugada Invalida. Espacio Ocupado")

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    vacias =[]
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] != "X" and board[fila][columna] != "O":
                vacias.append((fila,columna))
    return(vacias)

def victory_for(board):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    ganador = None
    if      board[0][0]==board[0][1]==board[0][2]:
        ganador = board[0][0]
    elif    board[1][0]==board[1][1]==board[1][2]:
        ganador = board[1][0]    
    elif    board[2][0]==board[2][1]==board[2][2]:
        ganador = board[2][0]
    elif    board[0][0]==board[1][0]==board[2][0]:
        ganador = board[0][0]
    elif    board[0][1]==board[1][1]==board[2][1]:
        ganador = board[0][1]
    elif    board[0][2]==board[1][2]==board[2][2]:
        ganador = board[0][2]
    elif    board[0][0]==board[1][1]==board[2][2]:
        ganador = board[0][0]
    elif    board[0][2]==board[1][1]==board[2][0]:
        ganador = board[0][2]
    vacias = make_list_of_free_fields(board)
    if ganador == "X":
        print("El ganador es la computadora")
        return 1
    elif ganador == "O":
        print("Ha ganado")
        return 1
    elif len(vacias) == 0:
        print("Empate")
        return 1
    else:
        print("El juego continua")
        return 0

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    posibles = make_list_of_free_fields(board)
    aleatorio = random.randrange(len(posibles))
    jugada = posibles[aleatorio]
    fila = int(jugada[0])
    columna = int(jugada[1])
    board[fila][columna] = "X"
    return 

import random
apagar = 0
board = [
        ["1","2","3"],
        ["4","X","6"],
        ["7","8","9"]
]
while apagar==0:
    display_board(board)
    apagar = victory_for(board)
    if apagar == 1:
        break
    enter_move(board)
    display_board(board)
    apagar = victory_for(board)
    if apagar == 1:
        break
    draw_move(board)