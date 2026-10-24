import math
from random import randint
from datetime import date
import calculadora

# Ejercicio 1: Área círculo redondeada
radio = 5
area = math.pi * (radio ** 2)
print("Área redondeada:", round(area, 2))

# Ejercicio 2: Lanzar dado 5 veces
lanzamientos = [randint(1, 6) for _ in range(5)]
print("Lanzamientos:", lanzamientos)

# Ejercicio 3: Uso de módulo propio
print("Suma con módulo calculadora:", calculadora.sumar(10, 5))

# Ejercicio 4: Fecha de hoy
print("Fecha de hoy:", date.today())