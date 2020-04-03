from sys import stdin

#(z^w)=>u
#~uV^vV^y

lista_negaciones = []
lista_condicionales = []
lista_letras = []
################LECTURA################
for x in stdin.readlines():
    if x[0] == "~":
        lista_negaciones.append(x)
        m = 0
        n = -1
        while m != -1:
            n = x[n+1:-1].find("V") + n + 1
            if x[n-1] not in lista_letras:
                lista_letras.append(x[n-1])
            if x[n+2] not in lista_letras:
                lista_letras.append(x[n+2])
            m = x[n+1:-1].find("V")
    if x[0] == "(":
        lista_condicionales.append(x)
        m = 0
        n = -1
        while m != -1:
            n = x[n+1:-1].find("^") + n + 1
            if x[n-1] not in lista_letras:
                lista_letras.append(x[n-1])
            if x[n+1] not in lista_letras:
                lista_letras.append(x[n+1])
            m = x[n+1:-1].find("^")
        n = x.find(">")
        if x[n+1] not in lista_letras:
            lista_letras.append(x[n+1])

###############ASIGNACION DE FALSE###############
SAT = dict((key,False) for key in lista_letras)

##############VERIFICACION DE CONDICIONALES##############
for condicional in lista_condicionales:
    n = condicional.find("^")
    m = 0
    izquierda = SAT[condicional[n-1]] and SAT[condicional[n+1]]
    while m != -1:
        n = condicional[n+1:-1].find("^") + n + 1
        m = condicional[n+1:-1].find("^")
        if m != -1:
            izquierda = izquierda and SAT[condicional[n+1]]
    n = condicional.find(">")
    derecha = SAT[condicional[n+1]]
    if izquierda == True and derecha == False:
        SAT[condicional[n+1]] = True

##############VERIFICACION DE CLAUSULAS NEGATIVAS###############
for negacion in lista_negaciones:
    n = negacion.find("V")
    valor_final = not SAT[negacion[n-1]] or not SAT[negacion[n+2]]
    m = 0
    while m != -1:
        n = negacion[n+1:-1].find("V") + n + 1
        m = negacion[n+1:-1].find("V")
        if m != -1:
            valor_final = valor_final or (not SAT[negacion[n+2]])
    if valor_final == False:
        print("La asignación no es satisfacible")
        break
print(SAT)
if valor_final == True:
    print("La asignación es satisfacible")
