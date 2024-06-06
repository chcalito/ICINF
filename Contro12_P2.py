nombres = []

for i in range(7):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

nombres_con_a = [nombre for nombre in nombres if nombre.endswith("a")]

print("Lista de nombres que terminan con 'a':")
for nombre in nombres_con_a:
    print(nombre)
