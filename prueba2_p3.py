capitales_paises = {}

print("Vamos a ingresar 5 capitales y sus países.")
for i in range(5):  
    capital = input(f"Ingrese la capital {i + 1}: ") 
    pais = input(f"Ingrese el país de la capital {capital}: ")  
    capitales_paises[capital] = pais  

print("Capitales y países ingresados:")
print(capitales_paises)

nombre_turista = input("Ingrese el nombre del turista: ")
capital_turista = input("Ingrese la capital de procedencia del turista: ")

pais_turista = capitales_paises.get(capital_turista, "desconocido")

print(f"El turista con el nombre {nombre_turista} viene de la capital {capital_turista} y su país es {pais_turista}.")
