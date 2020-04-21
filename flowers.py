from sys import stdin

def flowers(k,n):
    if n-k<0:
        return 1
    resultado = 1
    m = int(n/k) 
    resultado += m*(1+n-(k*(1+m))/2)
    return resultado
#lectura de entrada
arr = []
for x in stdin.readlines():
    arr.append(x)
aux = arr[0].find(" ")
t = int(arr[0][0:aux])
k = int(arr[0][aux:len(arr[0])])
for i in range(t):
    aux = arr[i+1].find(" ")
    a = int(arr[i+1][0:aux])
    b = int(arr[i+1][aux:len(arr[i+1])])
    acu = 0
    for j in range(a,b+1):
        #print("hola")
        acu += flowers(k,j)
    print(int(acu))
