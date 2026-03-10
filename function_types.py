def list_m(valores, incremento):
    for i in range(len(valores)):
        valores[i] = valores[i] + incremento


def calc_avg(valores):
    promedio = sum(valores) / len(valores)
    return promedio


def print_normalized(valores):
    print(valores)

datos = [2.0, 4.0, 6.0, 8.0]
prom = calc_avg(datos)
list_m(datos, -prom)
print_normalized(datos)
