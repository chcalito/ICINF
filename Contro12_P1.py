puntajes = []

for dia in range(1, 16):
    puntaje = int(input(f"Ingrese el puntaje del día {dia}: "))
    puntajes.append(puntaje)

print("Días con puntaje mayor o igual a 60:")
for dia, puntaje in enumerate(puntajes, start=1):
    if puntaje >= 60:
        print(f"Día {dia}")

print("\nDías con puntaje menor a 60:")
for dia, puntaje in enumerate(puntajes, start=1):
    if puntaje < 60:
        print(f"Día {dia}")
