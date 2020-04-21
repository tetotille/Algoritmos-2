from sys import stdin

def flowers(k,n):
    limite = int(n/k)+1
    valor = np.zeros(limite)
    valor[0] = 1
    x = np.arange(0,limite+1,1)
    valor[1:limite] = 1+n-(x[1:limite]*k)
    return valor.sum()

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
