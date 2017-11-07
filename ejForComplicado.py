'''Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y diga al final cuántos han sido pares y cuántos impares.


[7:31] 
CONTADOR DE PARES E IMPARES
¿Cuántos valores va a introducir? -1
¡Imposible!
CONTADOR DE PARES E IMPARES
¿Cuántos valores va a introducir? 5
Escriba el valor 1: 4
Escriba el valor 2: 3
Escriba el valor 3: 6
Escriba el valor 4: 8
Escriba el valor 5: 7
Ha escrito 3 números pares y 2 números impares
Gracias por su colaboración'''

print("CONTADOR DE PARES E IMPARES")
valores=int(input("Cuantos valores vas a introducr"))
if valores < 1:
	print("Imposible")
else:
	pares = 0 
	for i in range(1,valores):
		numero = int(input('Escribe el valor' + str(i)))
		if numero % 2 == 0:
			pares = pares + 1
			print("Ha escrito " + str(pares) + "numeros pares y " + str(valores - pares) + "numeros impares")
