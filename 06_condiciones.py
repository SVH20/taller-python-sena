# Ejercicio 1: Positivo, negativo o cero
num = -5
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")

# Ejercicio 2: Año bisiesto
anio = int(input("Ingresa un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es bisiesto")
else:
    print(f"{anio} no es bisiesto")

# Ejercicio 3: Saludo según la hora
hora = 14
if 0 <= hora < 12:
    print("Buenos días")
elif 12 <= hora < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")

# Ejercicio 4: Promedio de notas
n1, n2, n3 = 3.5, 4.0, 2.8
promedio = (n1 + n2 + n3) / 3
print(f"Promedio: {promedio:.2f} - {'Aprobó' if promedio >= 3.0 else 'Reprobó'}")