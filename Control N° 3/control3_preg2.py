def es_binario(var):
    for char in var:
        if char != '0' and char != '1':
            return False
    return True

cadena = input("Ingrese una cadena: ")

if es_binario(cadena):
    print(f"La cadena '{cadena}' es una expresión binaria.")
else:
    print(f"La cadena '{cadena}' no es una expresión binaria.")
