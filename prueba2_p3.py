capitales_paises = {}

print("ingresar 5 capitales y sus países.")
for i in range(5):
    capital = input("Ingrese la capital {}: ".format(i + 1)) 
    pais = input("Ingrese el país de la capital {}: ".format(capital)) 
    capitales_paises[capital] = pais  

print("Capitales y países ingresados:")
print(capitales_paises)

nombre_turista = input("Ingrese el nombre del turista: ")
capital_turista = input("Ingrese la capital de procedencia del turista: ")

pais_turista = "desconocido"
if capital_turista in capitales_paises:
    pais_turista = capitales_paises[capital_turista]

print("El turista con el nombre " + nombre_turista + " viene de la capital " + capital_turista + " y su país es " + pais_turista + ".")
