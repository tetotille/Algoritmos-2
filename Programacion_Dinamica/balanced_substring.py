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
    resultado = encontrar_resultado(resultados)
    return resultado

#MAIN
n,S = entrada()
resultado1 = encontrar_substring(n,S)
resultado2 = encontrar_substring(n,invertir_cadena(S))
if resultado1 > resultado2:
    print(resultado1)
else:
    print(resultado2)
