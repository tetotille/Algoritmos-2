#Social Constrains
from sys import stdin

global listaPermutaciones
listaPermutaciones = set()

def convertir(list):
    res = int("".join(map(str,list)))
    return res

def permute(a,l,r,x,y,c,condicion):
    if l == r:
        if condicion:
            if abs((a.index(x))-(a.index(y)))<=c:
                numero = convertir(a)
                listaPermutaciones.add(numero)
        else:
            if abs((a.index(x))-(a.index(y)))>=c:
                numero = convertir(a)
                listaPermutaciones.add(numero)
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r,x,y,c,condicion)
            a[l],a[i] = a[i],a[l]

def fact(n):
    res = 1
    for i in range(n):
        res = res * (i+1)
    return res

listaDef = set()
arr = []
for x in stdin.readlines():
    arr.append(x)
i = 0
while True:
    primeravez = True
    if "0 0" in arr[i]:
        break
    n,m = int(arr[i].split()[0]), int(arr[i].split()[1])
    for j in range(m):
        if len(arr[i+1+j].split()) == 3:
            a,b,c = int(arr[i+1+j].split()[0]),int(arr[i+1+j].split()[1]),int(arr[i+1+j].split()[2])
        else:
            a,b,c = int(arr[i+1+j].split()[0]),int(arr[i+1+j].split()[1]),0
        lista = list(range(n))
        listaPermutaciones = set()
        permute(lista,0,n-1,a,b,abs(c),c>0)
        
        if primeravez:
            listaDef = listaPermutaciones
        else:
            listaDef = listaDef.intersection(listaPermutaciones)
        primeravez = False
    if m == 0:
        print(fact(n))
    else:
        print(len(listaDef))
    i= i+m+1
    contador = 0
