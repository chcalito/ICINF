# Paso 1: Crear un diccionario vacío para guardar las capitales y sus países
capitales_paises = {}

# Paso 2: Pedir al usuario que ingrese 5 capitales con sus países
print("Vamos a ingresar 5 capitales y sus países.")
for i in range(5):
    capital = input("Ingrese la capital {}: ".format(i + 1))  # Pedimos la capital
    pais = input("Ingrese el país de la capital {}: ".format(capital))  # Pedimos el país de esa capital
    capitales_paises[capital] = pais  # Guardamos la capital y el país en el diccionario

# Mostrar el diccionario para verificar los datos ingresados (opcional)
print("Capitales y países ingresados:")
print(capitales_paises)

# Paso 3: Pedir el nombre del turista y la capital de procedencia
nombre_turista = input("Ingrese el nombre del turista: ")
capital_turista = input("Ingrese la capital de procedencia del turista: ")

# Paso 4: Encontrar el país correspondiente a la capital ingresada
pais_turista = "desconocido"
if capital_turista in capitales_paises:
    pais_turista = capitales_paises[capital_turista]

# Paso 5: Mostrar el mensaje final
print("El turista con el nombre " + nombre_turista + " viene de la capital " + capital_turista + " y su país es " + pais_turista + ".")
