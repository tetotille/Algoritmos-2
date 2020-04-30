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
    elif bits[-1][0] == "0":
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

def sumar_vector(vector,numero):
    for i in range(len(vector)):
        vector[i] = vector[i] + numero
    return vector

def resta_vector(vector,numero):
    for i in range(len(vector)):
        vector[i] = -vector[i] + numero
    return vector

def procesar_resultados(cadena1,cadena2,n,S):
    cadena1 = set(cadena1)
    cadena2 = set(cadena2)
    fusion = cadena1.union(cadena2)
    print(fusion)
    conjuntos = [[]]
    b = 1
    for num in fusion:
        if b == 1:
            conjuntos[-1].append(num)
            b = 0
        if not(((num + 1) in fusion) or ((num + 2) in fusion)):
            conjuntos[-1].append(num)
            conjuntos.append([])
            b = 1
    maximo = 0
    for conjunto in conjuntos:
        print(conjunto)
        if len(conjunto) != 0:
            auxiliar = encontrar_resultado(encontrar_substring(n,S[min(conjunto):max(conjunto)]))
            print(auxiliar  )
            if maximo < auxiliar: maximo = auxiliar
    return maximo



def substring(n,S):
    resultados = []
    resultados.append(encontrar_substring(n,S))
    print(resultados[0])
    S_inv = invertir_cadena(S)
    resultados.append(encontrar_substring(n,S_inv))
    resultados[1] = resta_vector(resultados[1],25)
    resultado_aux = (procesar_resultados(resultados[0],resultados[1],n,S))
    for i in range(len(resultados)):
        resultados[i] = encontrar_resultado(resultados[i])
    resultados.append(resultado_aux)
    return max(resultados)

#MAIN
n,S = entrada()
resultado = substring(n,S)
print(resultado)
