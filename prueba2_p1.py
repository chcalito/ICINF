notas = []

print("Ingrese las notas. Para finalizar, ingrese 0.")

while True:
    nota = float(input("Ingrese una nota: "))
    if nota == 0:
        break
    notas.append(nota)

cantidad_notas = len(notas)

if cantidad_notas > 0:
    promedio_notas = sum(notas) / cantidad_notas
else:
    promedio_notas = 0

notas_bajo_4 = len([nota for nota in notas if nota < 4.0])

notas_igual_o_mayor_4 = len([nota for nota in notas if nota >= 4.0])

print(f"1) Cantidad de notas: {cantidad_notas}")
print(f"2) Promedio de notas: {promedio_notas:.2f}")
print(f"3) Cantidad de notas bajo nota 4.0: {notas_bajo_4}")
print(f"4) Cantidad de notas igual o mayor que nota 4.0: {notas_igual_o_mayor_4}")
