from ganar import ganar
from copy import copy, deepcopy

## I: Dada una ficha seleccionada y una posición realiza el movimiento
def realizar_jugada(board,pos,pos2):
    if board[pos[0]][pos[1]] == 1:
        board[pos[0]][pos[1]] = 2
        board[pos2[0]][pos2[1]] = 1
    elif board[pos[0]][pos[1]] == 2:
        board[pos[0]][pos[1]] = 1
        board[pos2[0]][pos2[1]] = 2
## F: Dada una ficha seleccionada y una posición realiza el movimiento

## I: La inversa de la función realizar_jugada
def desrealizar_jugada(board,pos,pos2):
    if board[pos[0]][pos[1]] == 1:
        board[pos[0]][pos[1]] = 2
        board[pos2[0]][pos2[1]] = 0
    elif board[pos[0]][pos[1]] == 2:
        board[pos[0]][pos[1]] = 1
        board[pos2[0]][pos2[1]] = 0
## F: La inversa de la función realizar_jugada

def jugadas_posibles(tablero,pos): # Retorna una lista de posiciones de juego posible
    jugadas = []
    # Los try-except se agregan para evitar errores de índices en los bordes
    try:
        if  tablero[pos[0]][pos[1]-1] == 0 and pos[1]-1 >= 0:
            jugadas.append((pos[0],pos[1]-1))
    except:
        pass
    try:
        if tablero[pos[0]+1][pos[1]-1] == 0 and pos[1]-1 >= 0:
            jugadas.append((pos[0]+1,pos[1]-1))
    except:
        pass
    try:
        if tablero[pos[0]-1][pos[1]] == 0 and pos[0]-1 >= 0:
            jugadas.append((pos[0]-1,pos[1]))
    except:
        pass
    try:
        if tablero[pos[0]+1][pos[1]] == 0:
            jugadas.append((pos[0]+1,pos[1]))
    except:
        pass
    try:
        if tablero[pos[0]-1][pos[1]+1] == 0 and pos[0]-1 >= 0:
            jugadas.append((pos[0]-1,pos[1]+1))
    except:
        pass
    try:
        if tablero[pos[0]][pos[1]+1] == 0:
            jugadas.append((pos[0],pos[1]+1))
    except:
        pass
    return jugadas

## I: Define si se termina la partida, es decir, se gana, se pierde o se empata
def es_terminal(tablero):
    if ganar(tablero,1) or ganar(tablero,2):
        return True
    else:
        return False
## F: Define si se termina la partida, es decir, se gana, se pierde o se empata

## I: Obtener cadena a partir de una ficha
def obtener_cadena(tablero,pos,jugador):
    identificador = []
    if tablero[pos[0]][pos[1]] == jugador:#detecta si es una ficha negra
        fila = [pos]
        identificador = [pos[jugador-1]]
        while len(fila) != 0:
            ficha = fila.pop(0)
            tablero[ficha[0]][ficha[1]] = 3
            try: #para evitar los errores de índices
                if  tablero[ficha[0]][ficha[1]-1] == jugador: #si tiene un vecino del mismo color
                    fila.append((ficha[0],ficha[1]-1))
                    if ficha[1]-1 not in identificador and jugador == 2:
                        identificador.append(ficha[1]-1) #se guarda la fila o columna dependiendo del caso
            except:
                pass
            try:
                if tablero[ficha[0]+1][ficha[1]-1] == jugador:
                    fila.append((ficha[0]+1,ficha[1]-1))
                    if ficha[1]-1 not in identificador and jugador == 2:
                        identificador.append(ficha[1]-1)
                    elif ficha[0]+1 not in identificador and jugador == 1:
                        identificador.append(ficha[0]+1)
            except:
                pass
            try:
                if tablero[ficha[0]-1][ficha[1]] == jugador:
                    fila.append((ficha[0]-1,ficha[1]))
                    if ficha[0]-1 not in identificador and jugador == 1:
                        identificador.append(ficha[0]-1)
            except:
                pass
            try:
                if tablero[ficha[0]+1][ficha[1]] == jugador:
                    fila.append((ficha[0]+1,ficha[1]))
                    if ficha[0]+1 not in identificador and jugador == 1:
                        identificador.append(ficha[0]+1)
            except:
                pass
            try:
                if tablero[ficha[0]-1][ficha[1]+1] == jugador:
                    fila.append((ficha[0]-1,ficha[1]+1))
                    if ficha[1]+1 not in identificador and jugador == 2:
                        identificador.append(ficha[1]+1)
                    elif ficha[0]-1 not in identificador and jugador == 1:
                        identificador.append(ficha[0]-1)
            except:
                pass
            try:
                if tablero[ficha[0]][ficha[1]+1] == jugador:
                    fila.append((ficha[0],ficha[1]+1))
                    if ficha[1]+1 not in identificador and jugador == 2:
                        identificador.append(ficha[1]+1)
            except:
                pass
    return len(identificador)
## F: Obtener cadena a partir de una ficha

## I: Obtener la cadena vertical negra más larga
def obtener_vertical(tablero):
    maximo = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 2:
                maximo = max(maximo, obtener_cadena(tablero,(i,j),2))
    return maximo
## F: Obtener la cadena vertical negra más larga

## I: Obtener la cadena horizontal blanca más larga
def obtener_horizontal(tablero):
    maximo = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 1:
                maximo = max(maximo, obtener_cadena(tablero,(i,j),1))
    return maximo
## F: Obtener la cadena horizontal blanca más larga


def heuristica(tablero,jugador):
    value = -float("inf")
    cad_ver = obtener_vertical(deepcopy(tablero))
    cad_hor = obtener_horizontal(deepcopy(tablero))
    if jugador == 1:# Jugador blanco, linea horizontal
        try:
            value = cad_hor/cad_ver
        except:
            pass
    else:# Jugador negro, linea vertical
        try:
            value = cad_ver/cad_hor
        except:
            pass
    return value

def imprimir(tablero):
    for i in range(7):
        for j in range(7):
            print(tablero[j][i],"\t",end="")
        print("")
    print("")

## I: Encuentra todos los movimientos jugables
def encontrar_fichas(tablero,jugador):
    fichas = []
    for i in range(7):
        for j in range(7):
            jugadas = jugadas_posibles(tablero,(i,j))
            if tablero[i][j] == jugador and len(jugadas) != 0:
                fichas.append((i,j))
    return fichas
## F: Encuentra todos los movimientos jugables

def minimax (tablero, profundidad, jugador_maximizador,jugador):
    if jugador == 1: # Se obtiene el segundo jugador
        jugador2 = 2
    else:
        jugador2 = 1

    ## I: Verifica si el juego terminó o alcanzó el límite de cálculo
    #print(es_terminal(tablero,pos),pos)##########################################
    #######print("profundidad",profundidad)
    #######imprimir(tablero)
    if profundidad == 0 or es_terminal(deepcopy(tablero)):
        puntaje = heuristica(tablero,jugador)
        #######print("Puntaje: "+str(puntaje))
        #######imprimir(tablero)#########################################
        return puntaje
    ## F: Verifica si el juego terminó o alcanzó el límite de cálculo

    ## I: Busca las jugadas que dé mayor puntaje
    if jugador_maximizador == True:
        lista_fichas = encontrar_fichas(tablero,jugador2) # Primero encuentra todas las fichas movibles
        #######print("Lista_fichas: ",lista_fichas,end="\n\n")
        value = -float("inf")
        for ficha in lista_fichas:
            for hijo in jugadas_posibles(tablero,ficha):
                realizar_jugada(tablero,ficha,hijo)
                value = max(value,minimax(tablero,profundidad-1,False,jugador))
                desrealizar_jugada(tablero,ficha,hijo)
        return value
    ## F: Busca las jugadas que dé mayor puntaje

    ## I: Busca la jugada con menor puntaje ya que esa sería la mejor jugada del contrincante
    else: #Jugador minimizador
        lista_fichas = encontrar_fichas(tablero,jugador)
        ######print("Lista_fichasss: ",lista_fichas,end="\n\n")
        value = float("inf")
        for ficha in lista_fichas:
            for hijo in jugadas_posibles(tablero,ficha):
                realizar_jugada(tablero,ficha,hijo)
                value = min(value,minimax(tablero,profundidad-1,True,jugador))
                desrealizar_jugada(tablero,ficha,hijo)
        return value
    ## F: Busca la jugada con menor puntaje ya que esa sería la mejor jugada del contrincante


def bot(tablero,jugador,profundidad):
    if jugador == 1:
        jugador2 = 2
    else:
        jugador2 = 1
    lista_fichas = encontrar_fichas(tablero,jugador2)
    #######print(lista_fichas)
    ## I: Inicialización de variables
    ficha_elegida = (0,0)
    jugada_elegida = (0,0)
    maximo = 0
    ## F: Inicialización de variables

    ## I: Encuentra las jugadas posibles y obtiene la mejor de todas
    lista_jugadas = []
    for ficha in lista_fichas:
        lista_jugadas = jugadas_posibles(tablero,ficha)
        for pos in lista_jugadas:
            tablero_aux = deepcopy(tablero)
            realizar_jugada(tablero_aux,ficha,pos)
            posible_maximo = minimax(tablero_aux,profundidad,False,jugador)
            if maximo < posible_maximo:
                maximo = posible_maximo
                ficha_elegida = ficha
                jugada_elegida = pos
                print(maximo,ficha_elegida,jugada_elegida)
            desrealizar_jugada(tablero_aux,ficha,pos)

    ## F: Encuentra las jugadas posibles y obtiene la mejor de todas

    return ficha_elegida, jugada_elegida

if __name__ == "__main__":
    prueba = [[0,0,0,0,2,0,0],[0,1,2,1,1,0,0],[0,0,2,1,2,0,0],[1,2,2,1,0,0,0],[0,1,1,1,0,0,0],[0,1,2,0,0,0,0],[0,1,1,1,2,0,0]]
    print("horizontal",obtener_horizontal(deepcopy(prueba)))
    print("vertical",obtener_vertical(deepcopy(prueba)))
    imprimir(prueba)
