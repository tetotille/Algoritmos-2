def Pivot(N,B,A,b,c,v,l,e):
    #Creando las funciones objetivos a través de copias
    N_s = N.copy()
    B_s = B.copy()
    A_s = A.copy()
    b_s = b.copy()
    c_s = c.copy()
    v_s = v.copy()

    b_s[e] = b[l]/A[l][e]
    for j in N:
        if j != e:
            A_s[e][j] = A[l][j]/a[l][e]
    A_s[e][l] = 1/A[l][e]

    for i in B:
        if i != l:
            b_s[i] = b[i] - A[i][e]*b_s[e]
            for j in N:
                if j != e:
                    A_s[i][j] = A[i][j]
            A_s[i][l] = -A[i][e]*A_s[e][j]

    v_s = v+c[e] * b_s[e]

    for j in N:
        if j != e:
            c_s[j] = c[j] - c[e]*A_s[e][j]

    c_s[l] = -c[e]*A_s[e][l]
    N_s = N - set([e]).union(set([l]))
    B_s = B - set([l]).union(set([e]))
    return (N_s,B_s,A_s,b_s,c_s,v_s)


def minimizar(Delta,B):
    minimo = float("inf")
    i = 0
    for i in B:
        if Delta[i] < minimo:
            minimo = Delta[i]
            inidice = i
    return indice

def Initialize_simplex(A,b,c):
    k = b.index(min(b))
    n = len(b)
    m = len(c)
    if b[k] >= 0:
        return set([x+1 for x in range(n)]),set([x+n+1 for x in range(m)]),A,b,c,0
    l = n + k
    N,B,A,b,c,v = Pivot(N,B,A,b,c,v,l,0)
    if


def Simplex(A,b,c):
    N,B,A,b,c,v = Initialize_simplex(A,b,c)
    n = len(N)+len(B)
    Delta,X = [0]*n,[0]*n
    while max(c) > 0:
        e = c.index(max(c))
        for i in B:
            if A[i][e] > 0:
                Delta[i] = b[i]/A[i][e]
            else:
                Delta[i] = float("inf")
        l = minimizar(Delta,B)
        if Delta[l] == float("inf"):
            return "Unbounded"
        else:
            N,B,A,b,c,v = Pivot(N,B,A,b,c,v,l,e)
    for i in range(n):
        if i in B:
            X[i] = b[i]
        else:
            X[i] = 0
    return X

if __name__ == "__main__":
    A = [[-1,-1,-3],[-2,-2,-5],[-4,-1,-2]]
    b = [3,1,2]
    c = [30,24,36]
    print(Simplex(A,b,c))
