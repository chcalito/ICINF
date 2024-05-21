empleados_rango_bajo = 0
empleados_rango_alto = 0
gasto_total = 0

print("Ingrese los sueldos de los empleados mensualmente. Para terminar, ingrese -1.")

while True:
    sueldo = int(input("Ingrese el sueldo del empleado (en pesos): "))
    
    if sueldo == -1:
        break
    
    if sueldo <= 900000:
        empleados_rango_bajo += 1
    else:
        empleados_rango_alto += 1
    
    gasto_total += sueldo

print(f"Empleados que cobran entre $500.000 y $900.000: {empleados_rango_bajo}")
print(f"Empleados que cobran más de $900.000: {empleados_rango_alto}")
print(f"Gasto total en sueldos: ${gasto_total}")
