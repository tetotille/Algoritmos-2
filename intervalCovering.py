X = [9,8,7,6,5,4,3,2,1,0,9.3,9.6,2.1,5.6,7.7,1.5,3.3,4.9,6.9,8.1]

X.sort()
S = set()
while len(X) != 0:
    lista = [X[0]]
    while X[0]+1 >= X[1]:
        lista.append(X.pop(1))
        if len(X)==1:
            break
    X.pop(0)
    S.add(tuple(lista))

print(S)
