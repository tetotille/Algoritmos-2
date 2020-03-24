#FFT
import cmath
import math

def listaPares(a):
    res=[]
    for i in range(0,len(a),2):
        res.append(a[i])
    return res

def listaImpares(a):
    res=[]
    for i in range(1,len(a),2):
        res.append(a[i])
    return res

def imprimir(lista):
    for a in lista:
        print(a)

def FFT(a=[],w=0):
    n = len(a)
    r = [0]*n
    if int(w.real) == 1: return a
    a1 = listaPares(a)
    a2 = listaImpares(a)
    s1 = FFT(a1,w**2)
    s2 = FFT(a2,w**2)
    for j in range(n//2):
        r[j] = s1[j]+(w**j)*s2[j]
        r[j+n//2] = s1[j]-(w**j)*s2[j]
    return (r)

lista = [2,6,4,7,2,3,4,2]
N = len(lista)

w = cmath.exp(-2*math.pi*1j/N)

resultado = FFT(lista,w)
print("")
imprimir(resultado)
print("")