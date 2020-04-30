import math
def mulbin(x,y):
    if x & y == 0:
        return 0
    res = 0
    n = int(math.log2(y)) + 1
    for i in range(n):
        if y & 1 == 1:
            res = res + (x<<i)
        y = y>>1
    return res
    
a = input()
a = a.split()
x = int(a[0])
y = int(a[1])
resultado = mulbin(x,y)
print(resultado,end="")
