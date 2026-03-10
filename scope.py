int_value = None
str_value = None
def set_globals(algun_int, algun_str):
    global int_value, str_value
    int_value = algun_int
    str_value = algun_str

def get_globals():
    return (int_value, str_value)

print(get_globals())
set_globals(10,"Hello")
print(get_globals())


