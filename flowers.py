from sys import stdin

def flowers(lista,k,n):
    if n == 0:
        lista.append(lista[-1]+1)
        return lista
    else:
        lista = recursion(lista,k,n-1)
        if k <= n:
            lista = recursion (lista, k, n - k)
    return lista

#lectura de entrada
for x in stdin.readlines():

    
