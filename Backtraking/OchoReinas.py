#8 Queens
from sys import stdin
z = 0
def OchoReinas(n,lista,columna):
    global z
    m = 8
    global fila
    if n == 0:#Condicion de fin
        z = z+1
        imprimir(lista)
    else:
        
        for i in range(m):
            if 8 - n >= columna:
                bandera = 0
                for l in range(len(lista)):
                    x = len(lista)-l
                    if (i+1)==lista[l]+x:
                        bandera = 1
                    if (i+1) == lista[l]-x and lista[l]-x > 0:
                        bandera = 1
                if (i+1) in lista:
                    pass
                elif bandera == 1:
                    pass
                
                else:
                    lista.append(i+1)
                    OchoReinas(n-1,lista,columna)
                    lista.pop()
            else:
                bandera = 0
                for l in range(len(lista)-1):
                    x = len(lista)-l-1
                    if (i+1)==lista[l]+x:
                        bandera = 1
                    if (i+1) == lista[l]-x and lista[l]-x > 0:
                        bandera = 1
                if (i+1) in lista:
                    pass
                elif bandera == 1:
                    pass
                elif (fila-(i+1)) == (columna - len(lista)):
                    pass
                elif (fila-(i+1)) == (len(lista)- columna):
                    pass
                else:
                    a = lista.index(fila)
                    lista.insert(a,i+1)
                    OchoReinas(n-1,lista,columna)
                    lista.pop(a)
            
def imprimir(aux):
    global z
    if z <10:
        print("\n "+str(z),end="\t")
    else:
        print("\n"+str(z),end="\t")
    for i in range(len(aux)):
        if i <= 6:
            print(str(aux[i]), end=" ")
        else:
            print(str(aux[i]), end="")
def main():
    global fila
    global z
    text = stdin.read()
    x = text.split("\n\n")
    try:
        n = int(x[0])
    except:
        x = text.split("\n")
        n = int(x[0])

    for i in range(n):
        fila = int(x[i+1][0])
        columna = int(x[i+1][2])
        
        print("SOLN\t   COLUMN")
        print(" #\t1 2 3 4 5 6 7 8")
        z = 0
        OchoReinas(7,[fila],columna)
        print("\n")

main()