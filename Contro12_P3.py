palabras = []

while True:
    palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
    if palabra == "":
        break
    palabras.append(palabra)

if palabras:  
    longitud_maxima = max(len(palabra) for palabra in palabras)
    print("La palabra más larga tiene", longitud_maxima, "caracteres.")
else:
    print("No se ingresaron palabras.")
