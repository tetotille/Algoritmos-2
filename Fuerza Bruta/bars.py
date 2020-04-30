#Bars

from sys import stdin
from itertools import combinations

def sePuede(n,p,longitudes,setBarras):
    for i in range(p):
        a = tuple(combinations(longitudes,i+1))
        for tup in a:
            setBarras.add(sum(tup))
    if n in setBarras:
        return "YES"
    else:
        return "NO"



########### MAIN HE'I ##############
#Lectura
listaDef = set()
arr = []
for x in stdin.readlines():
    arr.append(x)

t = int(arr[0])
for i in range(1,t*3+1,3):
    n = int(arr[i])
    p = int(arr[i+1])
    longitudes = tuple(map(int,(arr[i+2].split())))
#Fin de lectura
    if n == 0:
        print("YES")
    else:
        resultado = sePuede(n,p,longitudes,set())
        print(resultado)