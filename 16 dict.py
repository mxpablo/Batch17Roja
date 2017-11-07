diccionario = {
'nombre':'Carlos',
'edad':'22',
'cursos':['Python','Flask']
}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])
print(diccionario['cursos'][0])
print(diccionario['cursos'][1])

dic = dict(nombre='Juan',apellido='Juarez',edad=22)
print(dic['nombre'])

print("--------------------------------")
for key,value in diccionario.items():
	print(key + " :" + str(value))

print("--------------------------------")
print(len(diccionario))

print("--------------------------------")
print(diccionario.keys())

print("--------------------------------")
print(diccionario.values())

print("--------------------------------")
print(diccionario.get("nombre","JUANITO"))

print("--------------------------------")
print(diccionario.get("nombree", "JUANITO"))

print("--------------------------------")
diccionario['key'] = 'value'
print(diccionario)

print("--------------------------------")
diccionario.pop('key')
print(diccionario)

print("--------------------------------")
lista_cursos = diccionario['cursos']
lista_cursos.append('Java')
print(lista_cursos)
print(diccionario)

print("--------------------------------")
diccionario2 = diccionario.copy()
print(diccionario2)

print("--------------------------------")
diccionario.update(dic)
print(diccionario)