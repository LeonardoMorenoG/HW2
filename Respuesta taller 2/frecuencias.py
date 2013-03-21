#permite pasar argumentos al programa, entre otros.
import sys
#read the file
infile = open (sys.argv[1],"r")
line = infile.readline()#read file char per char
lOC = []
#Guarda todos los caracteres en una lista
for item in line:
    lOC.append(item)
while line!="":
     line = infile.readline()
     for item in line:
         lOC.append(item)
infile.close()
#Elimina todos los caracteres no deseados de la lista
for item in lOC:
    if item=='\n':
        lOC.remove('\n')
for item in lOC:
    if item=='.':
        lOC.remove('.')
for item in lOC:
    if item==' ':
        lOC.remove(' ')
for item in lOC:
    if item==',':
        lOC.remove(',')
for item in lOC:
    if item==';':
        lOC.remove(';')
for item in lOC:
    if item==':':
        lOC.remove(':')
for item in lOC:
    if item=='-':
        lOC.remove('-')
#ordena la lista de caracteres alfabeticamente
lOC.sort()

#cuenta las letras en la lista
cuentaChar = {}
for char in lOC:
    cuentaChar[char]=cuentaChar.get(char,0)+1

#ordena ascendentemente los itmes del cuentaChar
itemsChar=cuentaChar.items()
itemsChar.sort(lambda x,y: cmp(x[1],y[1]))
#Invieerte el orden de la lista, descendente
itemsCharInv = itemsChar[::-1]
#Calcula el total de caracteres en el texto
sumaChar=0
for item in itemsChar:
    sumaChar+=item[1]
#Escribe el archivo deseado
nombreArchivo = "frecuencias_"
nombreArchivo+=sys.argv[1]
outfile=open(nombreArchivo,"w")
for item in itemsCharInv:
    outfile.write(item[0])
    outfile.write("	")
    outfile.write(str(item[1]*(100.0/sumaChar)))
    outfile.write('\n')
outfile.close()
