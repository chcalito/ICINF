TASA_CAMBIO_USD_CLP = 950.0

print("Por favor, ingrese 10 precios en pesos chilenos (CLP):")

precios_clp = []
for i in range(1, 11):  
    precio = float(input("Precio {}: ".format(i)))
    precios_clp.append(precio)

print("\nPrecios convertidos a USD:")
for precio_clp in precios_clp:
    precio_usd = precio_clp / TASA_CAMBIO_USD_CLP
    print("${}".format(precio_usd))

print("\nLista completa de precios en USD:")
for precio_usd in precios_clp:
    print("${}".format(precio_usd))
