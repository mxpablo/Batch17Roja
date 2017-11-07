x = int(input("Ingresa las cantidades a comprar: \n"))
precio = int(input("Ingresa el precio de dicho producto \n"))

producto = "Manzana"

if x < 6:
	total = x * precio 
	print(total)
else:
	total = x * precio * 0.95
	print(total)

