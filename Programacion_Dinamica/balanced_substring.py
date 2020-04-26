from sys import stdin

def entrada():
    arr = stdin.read().split("\n")
    n = int(arr[0])
    S = arr[1]
    return n,S

def encontrar_resultado(lista):
    if len(lista)==0:
        return 0
    lista.sort()
    c = 1
    maximo = 0
    for i in range(1,len(lista)):
        if lista[i] == lista[i-1]+1:
            c+=1
        else:
            c = 1
        if c > maximo:
            maximo = c
    return maximo

def comprobar_anterior(bit, bits):
    if len(bits) == 0:
        return False
    elif bits[-1][0] == bit:
        return False
    else:
        return True

def invertir_cadena(cadena):
    return cadena[::-1]

def encontrar_substring(n,S):
    bits = []
    resultados = []
    for i in range(len(S)):
        if comprobar_anterior(S[i],bits):
            bit = bits.pop()
            resultados.append(bit[1])
            resultados.append(i)
        else:
            bits.append((S[i],i))
    return resultados

def minimo(lista):
    try:
        return min(lista)
    except:
        return 0

def substring(n,S):
    resultados = encontrar_substring(n,S)
    resultados2 = encontrar_substring(n,invertir_cadena(S))
    resultado1 = encontrar_resultado(resultados)
    resultado2 = encontrar_resultado(resultados2)
    resultados.sort()
    a = len(S) - 1 - minimo(resultados2)
    resultado3 = 0
    for i in range(len(resultados)):
        resultado_aux = encontrar_resultado(encontrar_substring(n-resultados[i],S[resultados[i]+1:a+1]))
        if resultado_aux > resultado3:
            resultado3 = resultado_aux
    return max(resultado1,resultado2,resultado3)
#MAIN
n,S = entrada()
resultado = substring(n,S)
print(resultado)
