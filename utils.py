# FREEZE CODE BEGIN
def greet(name):
    """
    Return a greeting message for the given name.
    """
    return f"Hello, {name}!"


def flip(input_string):
    """
    Reverse the characters in the given string.
    """
    return input_string[::-1]


def count_letters(input_string, letter):
    """
    Count how many times a specific letter appears in a string.
    """
    count = 0
    for char in input_string:
        if char == letter:
            count += 1
    return count
# FREEZE CODE END


# --- TU CÓDIGO EMPIEZA AQUÍ ---

mensaje = input("Please type your message\n")

mensaje_invertido = flip(mensaje)

cantidad_a = count_letters(mensaje, "a")

mensaje_codificado = mensaje_invertido + str(cantidad_a)

print(f"Your encoded message is: {mensaje_codificado}")