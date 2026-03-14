from utils import *

# Paso 2 - Pedir el mensaje al usuario
message = input("Please type your message\n")

# Invertir el mensaje
flipped_message = flip(message)

# Contar las letras 'a' del mensaje original
a_count = count_letters(message, "a")

# Crear el mensaje codificado
encoded_message = flipped_message + str(a_count)

# Imprimir el resultado
print(f"Your encoded message is: {encoded_message}")