#!/usr/bin/python
# -*- coding: utf-8 -*-

a = int(input("Ingresa un número \n"))
b = int(input("Ingresa un número \n"))

c = a / b

print("Respuesta 1: " + str(c))

d = a % b

if d == 0:
	print("Respuesta 1: La división es exacta")
else:
	print("Respuesta 1: La división no es exacta")

if a < b:
	print("Respuesta 2: El primer número es menor al segundo número")
elif b < a:
	print("Respuesta 2: El segundo número es menor al primer número")
elif a = b:
	print("Respuesta 2: Los dos son iguales")

e = int(input("Ingresa el año actual\n"))
f = int(input("Ingresa un año cualquiera\n"))

if e < f:
	print("Faltan " + str(f - e) + " años ")
else: 
	print("Eso fue hace " + str(e -f) + " años")

g = int(input("Ingresa un primer número \n"))
h = int(input("Ingresa un segundo número \n"))
i = int(input("Ingresa un tercer número \n"))


if g == h and h == i:
	print("Los 3 números son iguales")
elif g == h or g == i or h == i:
	print("Si hay dos números iguales")
elif g != h and h != i:
	print("Los 3 números son diferentes")

if g > h and g > i:
	print("El primer número es mayor")
elif h > g and h > i:
	print("El segundo número es mayor")
elif i > g and i > h:
	print("El tercer número es el mayor")
