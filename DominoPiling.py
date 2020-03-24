#Autor: Jorge Tillería

w = input()
lista = w.split()
m = int(lista[0])
n = int(lista[1])

if n%2==0:
    N = int(n*m/2)
else:
    N = int((n-1)*m/2 + m/2)
print(N,end="")