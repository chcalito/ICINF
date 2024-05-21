total_preguntas = int(input("Ingrese el total de preguntas: "))
respuestas_correctas = int(input("Ingrese la cantidad de respuestas correctas: "))

porcentaje = (respuestas_correctas / total_preguntas) * 100

if porcentaje >= 95:
    nivel = "Nivel máximo"
elif porcentaje >= 70:
    nivel = "Nivel medio"
elif porcentaje >= 40:
    nivel = "Nivel regular"
else:
    nivel = "Fuera de nivel"

print(f"Porcentaje de respuestas correctas: {porcentaje:.2f}%")
print(f"Nivel obtenido: {nivel}")
