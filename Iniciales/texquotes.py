#autor: Jorge Luis Tillería Mereles

#Text Quotes 
#Problema 272 UVa

from sys import stdin
arr = []
for x in stdin.readlines():
    arr.append([y for y in x])
    
texto_corregido=""
b = 1
n = 0
for linea in arr:
    i = 0
    while i != len(linea):
        if linea[i] == '"':
            if b == 1:
                b = 2
                linea[i] = "`"
                linea.insert(i,"`")
            else:
                b = 1
                linea[i] = "'"
                linea.insert(i,"'")
            n = n + 1
        texto_corregido = texto_corregido + linea[i]
        a = i
        i = i+1
    n = 0
texto_corregido = texto_corregido.replace(" ","·")
print(texto_corregido,end="")