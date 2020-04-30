from sys import stdin

def lectura():
    arr = []
    for x in stdin.readlines():
        arr.append(x)
    return arr

def flowers(k,n):
    if n-k<0:
        return 1
    resultado = 1
    m = int(n/k)
    resultado += m*(1+n-(k*(1+m))/2)
    return resultado

def flowers_main(a,b,k):
    if a == b:
        return flowers(k,a)
    resultado = b-a + 1
    lamb = int(b/k)
    theta = flowers(k,a)-1
    n = b - a + 1
    #print(resultado)
    for i in range(1,lamb+1):
        an = b - i*lamb
        S = (n*(theta+an))/2
        resultado += S
        theta = 1
        n = b - (k*(i+1)) + 1
        #print(resultado)
    return resultado

arr = lectura()
aux = arr[0].find(" ")
t = int(arr[0][0:aux])
k = int(arr[0][aux:len(arr[0])])

for i in range(t):
    aux = arr[i+1].find(" ")
    a = int(arr[i+1][0:aux])
    b = int(arr[i+1][aux:len(arr[i+1])])

    resultado = flowers_main(a,b,k)
    print(int(resultado))
