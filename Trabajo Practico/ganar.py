#Este algoritmo verificará si existe un ganador en una jugada

def encontrar_vecinos(tablero,ficha,jugador): # Crea una lista de los vecinos y los retorna
    vecinos = []
    # Los try-except se agregan para evitar errores de índices en los bordes
    try:
        if  tablero[ficha[0]][ficha[1]-1] == jugador:
            vecinos.append((ficha[0],ficha[1]-1))
    except:
        pass
    try:
        if tablero[ficha[0]+1][ficha[1]-1] == jugador:
            vecinos.append((ficha[0]+1,ficha[1]-1))
    except:
        pass
    try:
        if tablero[ficha[0]-1][ficha[1]] == jugador:
            vecinos.append((ficha[0]-1,ficha[1]))
    except:
        pass
    try:
        if tablero[ficha[0]+1][ficha[1]] == jugador:
            vecinos.append((ficha[0]+1,ficha[1]))
    except:
        pass
    try:
        if tablero[ficha[0]-1][ficha[1]+1] == jugador:
            vecinos.append((ficha[0]-1,ficha[1]+1))
    except:
        pass
    try:
        if tablero[ficha[0]][ficha[1]+1] == jugador:
            vecinos.append((ficha[0],ficha[1]+1))
    except:
        pass
    return vecinos

def exploracion(tablero, fila, posicion,jugador):

    while len(fila) != 0: #Si la fila se termina es porque nadie ganó
        ficha = fila.pop(0)
        tablero[ficha[0]][ficha[1]] = 3

        ## I: Condición de fin si se encontró algún valor del sitio opuesto
        if posicion == 0: #Si está a la izquierda o arriba
            if jugador == 1: #Jugador blanco
                if ficha[0] == 6: return 1
            else: #jugador negro
                if ficha[1] == 6: return 1
        else: #Está abajo o a la derecha
            if jugador == 1: #Jugador blanco
                if ficha[0] == 0: return 1
            else: #jugador negro
                if ficha[1] == 0: return 1
        ## F: Condición de fin si se encontró algún valor del sitio opuesto

        ## I: Árbol de búsqueda
        vecinos = encontrar_vecinos(tablero,ficha,jugador)
        for vecino in vecinos:
            if vecino not in fila:
                fila.insert(0,vecino)
            else:
                fila.remove(vecino)
                fila.insert(0,vecino)
        ## F: Árbol de búsqueda
    return 0

## I: Se convierte el conjunto de valores iniciales en una lista de tuplas
def procesar(raiz,jugador,valor):
    lista = []
    if jugador == 1:
        for indice in raiz:
            lista.append((valor,indice))
    else:
        for indice in raiz:
            lista.append((indice,valor))
    return lista
## F: Se convierte el conjunto de valores iniciales en una lista de tuplas

#Jugador es 1 si fue el turno de blanco y 2 si fue el turno de negro
def ganar(tablero,jugador):
    bandera1 = 0
    bandera2 = 0
    raiz1 = set()
    raiz2 = set()
    for i in range(7):
        
        ## I: verificador de condición de fichas extremas negro
        if jugador == 1:
            if tablero[0][i] == 1:
                bandera1 = 1
                raiz1.add(i)
            if tablero[6][i] ==1:
                bandera2 = 1
                raiz2.add(i)
        ## F: verificador de condición de fichas extremas negro

        ## I: verificador de condición de fichas extremas negro
        else:
            if tablero[i][0] == 2:
                bandera1 = 1
                raiz1.add(i)
            if tablero[i][6] == 2:
                bandera2 = 1
                raiz2.add(i)
        ## F: verificador de condición de fichas extremas negro

    ## I: algoritmo verificador
    if bandera1 and bandera2:#se toma el conjunto de fichas en el extremo más pequeño para empezar
        if len(raiz1) < len(raiz2):
            fila = procesar(raiz1,jugador,0)
            return exploracion(tablero,fila,0,jugador)
        else:
            fila = procesar(raiz2,jugador,6)
            return exploracion(tablero,fila,6,jugador)
    ## F: algoritmo verificador
