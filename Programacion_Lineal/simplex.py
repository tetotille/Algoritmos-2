#Maximizar

#z = 10X1 + 20X2
#restricciones
#4X1+2X2 <= 20
#8X1 + 8X2 <= 20
#2X2 <= 10
#matriz = [[0,4,2,1,0,0,20],[0,8,8,0,1,0,20],[0,0,2,0,0,1,10],[1,-10,-20,0,0,0,0]]

#X1, X2 variables básicas
#variables de restriccion S1,S2 y S3
def resta(V1,V2):
    V3 = []
    for i in range(len(V1)):
        V3.append(V1[i]-V2[i])
    return V3


class Simplex:
    def __init__(self):
        self.tabla = []
        self.solucion_optima = False
        self.fila_pivot = 0
        self.columna_pivot = 0
        self.tabla2 = []

#recibe las restricciones y las convierte en el formato de tabla simplex
    def insertar_restricciones(self,matriz,condicion):
        n = len(matriz)
        for i in range(n):
            Svar = [0]*n
            Svar[i] = 1
            self.tabla.append([0]+matriz[i][0:-1]+Svar+[matriz[i][-1]])
        self.tabla.append([1]+condicion+[0]*4)

    def encontrar_columna_pivot(self,n):
        self.columna_pivot = 1+self.tabla[-1].index(min(self.tabla[-1][1:n]))
        return self.columna_pivot

    def encontrar_fila_pivot(self):
        minimo = float("inf")
        for i in range(len(self.tabla)-1):
            if minimo > self.tabla[i][-1]/self.tabla[i][self.columna_pivot]:
                minimo = self.tabla[i][-1]/self.tabla[i][self.columna_pivot]
                self.fila_pivot = i
        return self.fila_pivot

    def encontrar_tabla2(self):
        pivot = self.tabla[self.fila_pivot][self.columna_pivot]
        self.tabla2 = self.tabla.copy()
        #se halla la fila entrante dividiendo la fila del pivot por el pivot
        self.tabla2[self.fila_pivot] = [x/pivot for x in self.tabla2[self.fila_pivot]]
        #para todos los que no son fila pivot se multiplica por el elemento de la columna pivot correspondiente
        #con la fila pivot y ese resultado se le resta a la fila vieja
        filaPivot = self.tabla2[self.fila_pivot] #variable auxiliar para no tener que escribir tanto
        for i in range(len(self.tabla2)):
            if i != self.fila_pivot:
                multiplicacion = [self.tabla2[i][self.columna_pivot]*x for x in filaPivot]
                self.tabla2[i] = resta(self.tabla2[i],multiplicacion)#ejecuta la resta vectorial

    def tiene_solucion_optima(self):
        if min(self.tabla2[-1]) >=0:
            self.solucion_optima = True
        return self.solucion_optima

    def imprimir_solucion(self):
        print("\nX"+str(self.fila_pivot+1)+" = ",self.tabla2[self.fila_pivot][-1])
        print("Z = ",self.tabla2[-1][-1])
    #Hace el procedimiento de maximizar
def maximizar(matriz,condicion):
    sistema = Simplex()
    n = len(condicion)
    sistema.insertar_restricciones(matriz,condicion)#convierte la entrada en una tabla simplex
    print("Simplex")
    for a in sistema.tabla: print(a)
    columna = sistema.encontrar_columna_pivot(n)
    fila = sistema.encontrar_fila_pivot()
    sistema.encontrar_tabla2()
    print("\nSimplex_2")
    for a in sistema.tabla2: print(a)
    if sistema.tiene_solucion_optima():
        sistema.imprimir_solucion()
    else:
        print("El sistema no posee solución óptima")

if __name__=="__main__":
    #maximizar Z = 10X1 + 20X2
    condicion = [-10,-20]
    condicion2 = [-3,-1,-2]
    condicion3 = [-1,-3]
    #restricciones
    ## 4X1 + 8X2 <= 20
    ## 8X1 + 8X2 <= 20
    ##       2X2 <= 10
    restricciones = [[4,2,20],[8,8,20],[0,2,10]]
    restricciones2 = [[1,1,3,30],[2,2,5,24],[4,1,2,36]]
    restricciones3 = [[1,-1,8],[-1,-1,-3],[-1,4,2]]
    maximizar(restricciones,condicion)
    maximizar(condicion3,restricciones3)
