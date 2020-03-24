#The Knight Tour
from sys import stdin

def crearTablero(n):
    cadena = ""
    lista = []
    listofzeros = [0]*n
    for i in range(n):
        cadena = cadena+str(i)
        lista.append(listofzeros.copy())
    tablero = dict(zip(cadena,lista))
    return tablero

def Imprimir(diccionario):
    for l in diccionario:
        for i in diccionario[l]:
            print("\t"+str(i),end="")
        print("")
        
def condicionFIN(x,y,tablero):
    x_nuevo = str(int(x)+1)
    y_nuevo = y+2
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#1
            return True
    x_nuevo = str(int(x)+2)
    y_nuevo = y+1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#2
            return True
    x_nuevo = str(int(x)+2)
    y_nuevo = y-1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#3
            return True
    x_nuevo = str(int(x)+1)
    y_nuevo = y-2
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#4
            return True
    x_nuevo = str(int(x)-1)
    y_nuevo = y-2
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#5
            return True
    x_nuevo = str(int(x)-2)
    y_nuevo = y-1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#6
            return True
    x_nuevo = str(int(x)-2)
    y_nuevo = y+1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#7
            return True
    x_nuevo = str(int(x)-1)
    y_nuevo = y+2
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1)):
        aux = tablero[x_nuevo][y_nuevo]
        if aux==1:#8
            return True
    return False

def sortThird(val): 
    return val[2]

def ordenar(lista):
    lista = list(lista)
    lista.sort(key = sortThird)
    return lista

def Heuristica(x_ent,y_ent,n):
    x = min(int(x_ent)+1,n-int(x_ent))
    y = min(y_ent+1,n-y_ent)
    if x==1:
        if y==1:
            return 2
        elif y == 2:
            return 3
        else:
            return 4
    if y == 1:
        if x==2:
            return 3
        else:
            return 4
    if x == 2:
        if y == 2:
            return 4
        else:
            return 6
    if y == 2:
        return 6
    return 8

def esInteligente(x,y,tablero,ben):
    global x_elegido
    global y_elegido
    n = len(tablero)
    contador = 0
    if ben == True:
        return True
    x1 = str(int(x_elegido) - 2)
    x2 = str(int(x_elegido) - 1)
    x3 = str(int(x_elegido) + 1)
    x4 = str(int(x_elegido) + 2)
    
    y1 = y_elegido - 2
    y2 = y_elegido - 1
    y3 = y_elegido + 1
    y4 = y_elegido + 2
    
    
    try:
        if tablero[x1][y3] == 1:
            contador +=1
    except:
        pass
    try:
        if tablero[x1][y2] == 1:
            contador+=1
    except:
        pass
    try:
        if tablero[x2][y1] == 1:
            contador+=1
    except:
        pass
    try:
        if tablero[x2][y4] == 1:
            contador +=1
    except:
        pass
    try:
        if tablero[x3][y1] == 1:
            contador+=1
    except:
        pass
    try:
        if tablero[x3][y4] == 1:
            contador +=1
    except:
        pass
    
    try:
        if tablero[x4][y3] == 1:
            contador +=1
    except:
        pass
    try:
        if tablero[x4][y2] == 1:
            contador+=1
    except:
        pass
    if condicionFIN(x,y,tablero):
        contador+=1
    if contador >= 8:
        return False
    else:
        return True
    

def siguienteMovimiento(x,y,tablero,ben):
    x_nuevo = str(int(x)+1)
    y_nuevo = y+2
    listaMov = set()
    if (int(x_nuevo)>=0 and int(x_nuevo)<=len(tablero)-1) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#1
            listaMov.add((x_nuevo,y_nuevo,a))
    x_nuevo = str(int(x)+2)
    y_nuevo = y+1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#2
            listaMov.add((x_nuevo,y_nuevo,a))
    x_nuevo = str(int(x)+2)
    y_nuevo = y-1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#3
            listaMov.add((x_nuevo,y_nuevo,a))
    x_nuevo = str(int(x)+1)
    y_nuevo = y-2
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#4
            listaMov.add((x_nuevo,y_nuevo,a))
    x_nuevo = str(int(x)-1)
    y_nuevo = y-2
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#5
            listaMov.add((x_nuevo,y_nuevo,a))
    x_nuevo = str(int(x)-2)
    y_nuevo = y-1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#6
            listaMov.add((x_nuevo,y_nuevo,a))
    x_nuevo = str(int(x)-2)
    y_nuevo = y+1
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#7
            listaMov.add((x_nuevo,y_nuevo,a))
    x_nuevo = str(int(x)-1)
    y_nuevo = y+2
    if (int(x_nuevo)>=0 and int(x_nuevo)<=(len(tablero)-1)) and (y_nuevo>=0 and y_nuevo<=(len(tablero)-1) and esInteligente(x_nuevo,y_nuevo,tablero,ben)):
        aux = tablero[x_nuevo][y_nuevo]
        a = Heuristica(x_nuevo,y_nuevo,len(tablero))
        if aux==0:#8
            listaMov.add((x_nuevo,y_nuevo,a))
    listaMov=ordenar(listaMov)
    return listaMov


def knightTour(n,x,y,tablero):
    global limit
    global bandera
    if bandera != 1:
        if n == 1:
            if condicionFIN(x,y,tablero)==True:
                Imprimir(tablero)
                print("")
                bandera = 1
        else:
            ben = False
            if n == 2 : ben = True
            movimientosPosibles = siguienteMovimiento(x,y,tablero,ben)
            for mov in movimientosPosibles:
                tablero[mov[0]][mov[1]] = limit+2-n
                knightTour(n-1,mov[0],mov[1],tablero)
                tablero[mov[0]][mov[1]] = 0

texto = stdin.read()
vectorr = texto.split("\n")
#vectorr = ["5 1 1","6 1 1","6 2 2"]
for lala in vectorr:
    vec = lala.split()
    n = int(vec[0])
    tablero = crearTablero(n)
    tablero2 = crearTablero(n)
    x = str(int(vec[1])-1)
    y = int(vec[2])-1
    limit = n*n
    tablero[x][y] = 1
    x_elegido = x
    y_elegido = y
    tablero2[x][y] = 1
    bandera = 0
    knightTour(limit,x,y,tablero)
    if bandera == 0:
        print("No circuit tour.\n")
    tablero = 0
    tablero2 = 0