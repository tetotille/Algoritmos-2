#SAT
from sys import stdin

def imprimir(n,m):
    cadena = ""
    #print(n)
    while m >0:
        if (n & 1)==1:
            cadena = "T "+cadena
        else:
            cadena = "F "+cadena
        n = n>>1
        m = m-1
    print(cadena)
arr = []
################ MAIN ##############
#Lectura de datos
arr2 = stdin.readline()
la=0
lala=1
for i in range(len(arr2)):
    if arr2[i]=="x":
        la = max(la,int(arr2[i+1]))
    if arr2[i]=="^":
        lala+=1
arr2 = arr2.replace("~","not ")
arr2 = arr2.replace("^"," and"+"\n")
arr2 = arr2.replace("v"," or ")


arr.append(str(lala)+" "+str(la))
arr.extend(list(arr2.split("\n")))
datos = tuple(arr[0].split())
n = int(datos[0])
m = int(datos[1])
todo = []
for i in range(n):
    linea = arr[i+1]
    listaX = []
    ax = linea.find("x")
    while ax != -1:
        
        if(linea.find("not",ax-5,ax)!=-1):
            listaX.append(-int(linea[ax+1]))
        else:
            listaX.append(int(linea[ax+1]))
        ax = linea.find("x",ax+1,-1)
    todo.append(tuple(listaX))
#Fin de lectura    
resultado2 = True
contador = 0
#elaboracion de comparaciones
for i in range((1<<m)-1,-1,-1):
    x=[]
    for j in range(m):
        x.append(((i>>j)&1)|0)
    x.reverse()
    resultado2 = True
    for listaa in todo:
        resultado1 = False
        for indice in listaa:
            if indice<0:
                aux = not(x[abs(indice)-1])
                resultado1 = resultado1 | aux
            else:
                aux = ((x[indice-1]))
                resultado1 = resultado1 | aux
            resultado2 = resultado2 & resultado1
    if (resultado2):
        ress = i
        imprimir(ress,m)
        break
if resultado2 == False:
    print("impossible")
    
