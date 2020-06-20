from ganar import ganar

## I: Define si se termina la partida, es decir, se gana, se pierde o se empata
def es_terminal(tablero,pos):
    if ganar(tablero,1) or ganar(tablero,2):
        return True
    else:
        return False
## F: Define si se termina la partida, es decir, se gana, se pierde o se empata

def heuristica(tablero,jugador):
    contador = 0
    for vector in tablero:
        for valor in vector:
            if valor == jugador: contador+=1
    return contador


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


def minimax (tablero, pos, profundidad, jugador_maximizador,jugador):
    ## I: Verifica si el juego terminó o alcanzó el límite de cálculo
    if profundidad == 0 or es_terminal(tablero,pos):
        return heuristica(tablero,jugador)
    ## F: Verifica si el juego terminó o alcanzó el límite de cálculo

    ## I: Busca las jugadas que dé mayor puntaje
    if jugador_maximizador:
        value = -float("inf")
        for hijo in jugadas_posibles(tablero,pos):
            value = max(value,minimax(tablero,hijo,profundidad-1,False,jugador))
        return value
    ## F: Busca las jugadas que dé mayor puntaje

    ## I: Busca la jugada con menor puntaje ya que esa sería la mejor jugada del contrincante
    else: #Jugador minimizador
        value = float("inf")
        for hijo in jugadas_posibles(tablero,pos):
            value = min(value,minimax(tablero,hijo,profundidad-1,True,jugador))
        return value
    ## F: Busca la jugada con menor puntaje ya que esa sería la mejor jugada del contrincante

## I: Encuentra todos los movimientos jugables
def encontrar_fichas(tablero,jugador):
    fichas = []
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == jugador and len(jugadas_posibles(tablero,(i,j))) != 0:
                fichas.append((i,j))
    return fichas
## F: Encuentra todos los movimientos jugables

def bot(tablero,jugador,profundidad):
    lista_fichas = encontrar_fichas(tablero,jugador)

    ## I: Inicialización de variables
    ficha_elegida = (0,0)
    jugada_elegida = (0,0)
    maximo = -float("inf")
    ## F: Inicialización de variables

    ## I: Encuentra las jugadas posibles y obtiene la mejor de todas
    for ficha in lista_fichas:
        lista_jugadas = jugadas_posibles(tablero,ficha)
        for pos in lista_jugadas:
            posible_maximo = minimax(tablero,pos,profundidad,True,jugador)
            if maximo < posible_maximo:
                maximo = posible_maximo
                ficha_elegida = ficha
                jugada_elegida = pos
    ## F: Encuentra las jugadas posibles y obtiene la mejor de todas

    return ficha_elegida, jugada_elegida
