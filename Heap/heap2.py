

def parent(i):
    return int((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def min_heapify(A,i=0):
    l = left(i)
    r = right(i)
    if l < len(A):
        if A[l].d < A[i].d:
            smallest = l
        else:
            smallest = i
    else:
        smallest = i
    if r < len(A):
        if A[r].d < A[smallest].d:
            smallest = r
    if smallest != i:
        aux = A[i]
        A[i] = A[smallest]
        A[smallest] = aux
        min_heapify(A,smallest)


def minimum(A):
    return A[0]

def extract_min(A):
    if len(A) < 1:
        print("error: heap underflow")
        close()
    min = A[0]
    A.pop(0)
    if len(A)!=0:
        min_heapify(A,0)
    return min

def heap_decrease_key(A,i,key):
    if key > A[i].d:
        print("error: new key is greater than current key")
        exit()
    A[i].d = key
    while i > 1 and A[parent(i)].d > A[i].d:
        aux = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = aux
        i = parent(i)

def min_heap_insert(A,key):
    A.append(float("inf"))
    heap_decrease_key(A,len(A),key)
