from inpHeXionWindow import start_window
from ganar import ganar
from copy import copy, deepcopy
from inPhexBot import bot

### InPhexion                       ###
### Versión: 1.0.0                  ###
### Creador: Jorge Tillería         ###
### Correo: jtilleria@fiuna.edu.py  ###



def main(window):
### I: declaración del tablero ###
    board = []
    for i in range(7):
        board.append([])
        for j in range(7):
            board[i].append(0)
    end_game = 0

    window.print_board(board)
### F: declaración del tablero ###

### I: Primera jugada blanca ###
    pos = window.scan_position()
    board[pos[0]][pos[1]] = 1
    window.print_board(board)
### F: Primera jugada blanca ###

    ultima_jugada = 2 #1 para blanco, 0 para negro
    while True:
        if ultima_jugada == 1:
            print("Turno de jugador Negro")
        else:
            print("\nTurno del jugador Blanco")
        if ultima_jugada != 2:
            pos = window.scan_position() #seleccion de pieza
        else:
            pos, pos2 = bot(deepcopy(board),2,4)

        ## I: Verificación de si la pieza que se tocó es correcta
        if ultima_jugada == 1 and board[pos[0]][pos[1]] != 1: continue
        elif ultima_jugada == 0 and board[pos[0]][pos[1]] != 2: continue
        ## F: Verificación de si la pieza que se tocó es correcta

        ## I: Verificación de si el destino es válido
        if ultima_jugada != 2:
            bandera_posicion = 0
            bandera_deseleccion = 0
            while bandera_posicion == 0:
                pos2 = window.scan_position() #selección de destino
                #se verifica si se des-seleccionó
                if board[pos2[0]][pos2[1]] == board[pos[0]][pos[1]]:
                    bandera_deseleccion = 1
                    break
                #se verifica que esté en una de las proximidades y no esté ocupado
                #por otra pieza
                if  ((pos[0]-1 == pos2[0] and pos[1] == pos2[1]) or
                    (pos[0]-1 == pos2[0] and pos[1]+1 == pos2[1]) or
                    (pos[0] == pos2[0] and pos[1]-1 == pos2[1]) or
                    (pos[0] == pos2[0] and pos[1]+1 == pos2[1]) or
                    (pos[0]+1 == pos2[0] and pos[1]-1 == pos2[1]) or
                    (pos[0]+1 == pos2[0] and pos[1] == pos2[1])) and board[pos2[0]][pos2[1]]==0:
                    bandera_posicion = 1
            if bandera_deseleccion == 1:
                continue
        ## F: Verificación de si el destino es válido

        print("Ficha seleccionada: ",pos)
        print("Posición de movida: ",pos2)

        ## I: Jugada Jugador negro
        if board[pos[0]][pos[1]] == 1:
            board[pos[0]][pos[1]] = 2
            board[pos2[0]][pos2[1]] = 1
            ultima_jugada = 0
            if ganar(deepcopy(board),2):
                end_game = 2
        ## F: Jugada Jugador negro

        ## I: Jugada Jugador blanco
        elif board[pos[0]][pos[1]] == 2:
            board[pos[0]][pos[1]] = 1
            board[pos2[0]][pos2[1]] = 2
            ultima_jugada = 2
            if ganar(deepcopy(board),1):
                end_game = 1

        ## F: Jugada Jugador blanco

        window.print_board(board)

    ## I: Condición de fin de juego y publicación de ganador
        if end_game:
            break
    if end_game == 1:
        input("Ganó el jugador blanco")
    else:
        input("Ganó el jugador negro")

    ## F: Condición de fin de juego y publicación de ganador

    window.close()

start_window(main)
