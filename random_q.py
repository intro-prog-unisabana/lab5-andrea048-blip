import random

# Establecer la semilla fija
random.seed(123)

# Solicitar datos al usuario
start = int(input("Enter the start value:\n"))
end = int(input("Enter the end value:\n"))

# Generar número aleatorio en el rango (inclusive)
random_number = random.randint(start, end)

# Imprimir resultado
print(f"Generated random number: {random_number}")