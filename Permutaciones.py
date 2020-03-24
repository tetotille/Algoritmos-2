#Permutaciones

def Permutar(lista,n):
    if n == 1:
        lista.reverse()
        print(lista)
        lista.reverse()
    else:
        for i in range(n):
            aux = lista[i] 
            lista[i] = lista[n-1]
            lista[n-1] = aux
            #print("ALGO ",end="")
            #print(lista)
            Permutar(lista,n-1)
            aux = lista[i] 
            lista[i] = lista[n-1]
            lista[n-1] = aux



a = input("Introduzca una cadena de bits sin espacios\n")
lista = []
for i in a:
    lista.append(i)
Permutar(lista,len(lista))
