TASA_CAMBIO_USD_CLP = 950.0

precios_clp = []

print("Por favor, ingrese 10 precios en pesos chilenos (CLP):")

for i in range(10):
    precio = float(input("Ingrese el precio " + str(i + 1) + ": "))
    precios_clp.append(precio)

precios_usd = []
for precio_clp in precios_clp:
    precio_usd = precio_clp / TASA_CAMBIO_USD_CLP
    precios_usd.append(precio_usd)

print("Precios convertidos a USD:")
for precio_usd in precios_usd:
    print("$" + "%.2f" % precio_usd)

print("Lista completa de precios en USD:")
print(["$" + "%.2f" % precio_usd for precio_usd in precios_usd])
