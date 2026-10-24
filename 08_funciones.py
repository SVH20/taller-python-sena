# Ejercicio 1: es_par
def es_par(n):
    return n % 2 == 0

# Ejercicio 2: area_circulo
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

# Ejercicio 3: Mayor de una lista sin max()
def obtener_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

# Ejercicio 4: Factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Pruebas
print("es_par(4):", es_par(4))
print("area_circulo(5):", area_circulo(5))
print("obtener_mayor([3, 12, 5, 25]):", obtener_mayor([3, 12, 5, 25]))
print("factorial(5):", factorial(5))