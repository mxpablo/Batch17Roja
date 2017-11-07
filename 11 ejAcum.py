print("Del 1 al 100")
cuenta = 0
for i in range(1,101):
	print(i)

print("Del 1 al 100 números pares")
cuenta = 0
for i in range(1,101):
	if i % 2 == 0:
		print(i)

print("La tercera E en ELEFANTE")
var = "ELEFANTE"
cuenta = 0
for i in var:
	if i == "E":
		cuenta = cuenta + 1
		if cuenta == 3:
			print("La encontré")

