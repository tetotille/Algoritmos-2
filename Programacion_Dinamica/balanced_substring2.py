from sys import stdin
import string

def entrada():
    arr = stdin.read().split("\n")
    n = int(arr[0])
    S = arr[1]
    return n,S

def minimo(n,m):
    if n > m:
        return m,"0"
    else:
        return n,"1"

def listar_posiciones(cadena,n,letra):
    lista = []
    a = cadena.find(letra)
    for i in range(n):
        lista.append(a)
        a = cadena[a+1:len(cadena)].find(letra) + a + 1
    return lista

def contar(bits):
    ceros = string.count(bits,"0")
    unos = string.count(bits,"1")
    print(ceros,unos)
    print(bits)
    if ceros == unos:
        return unos
    else:
        return 0

def substring(n,S):
    n = string.count(S,"1")
    n,es = minimo(n,len(S)-n)
    listados = listar_posiciones(S,n,es)
    resultado = 0
    for i in range(n):
        posicion = listados[i]
        resultado_aux = contar(S[posicion:(posicion+n-i)*2])
        if resultado < resultado_aux:
            resultado = resultado_aux
    return resultado

n,S = entrada()
resultado = substring(n,S)
print(resultado)
