lista = []
for i in range(0,100):
	lista.append(i+1)
print(lista)

numero = int(input("Escribe un número \n"))
lista2 = []
for i in range(1,11):
	lista2.append (numero*i)
print(lista2)

lista3=[4,76,3,12,65,3]
lista4=[234,222,523,65]

lista5 = []
lista5.extend(lista3)
lista5.extend(lista4)
print(lista5)

suma = 0
for i in lista5:
	suma += i
print(suma)

lista6=[4,76,3,12,65,3]
lista7=[234,222,523,65]

lista8 = lista6 + lista7

valor = 0 
for i in lista8:
	valor = valor + i
print(valor)