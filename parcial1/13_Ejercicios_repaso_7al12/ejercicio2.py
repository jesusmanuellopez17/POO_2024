# 2.- Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for



lista = []
contador = 0

while len(lista) < 120:
    lista.append(contador)
    contador += 1


for valor in lista:
    print(valor)





