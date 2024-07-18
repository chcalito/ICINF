def digitos(num):
    num_str = str(num)
    
    return len(num_str)

numero = input("Ingrese un número: ")

try:
    numero = int(numero)
    print(f"El número {numero} tiene {digitos(numero)} dígitos.")
except ValueError:
    print("Por favor, ingrese un número válido.")
