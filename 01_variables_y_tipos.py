# 1. Variables personales
nombre = "Santiago"
edad = 23
estatura = 1.80
es_aprendiz = True
print(nombre, edad, estatura, es_aprendiz)

# 2. Tipo de cada variable
print(type(nombre), type(edad), type(estatura), type(es_aprendiz))

# 3. Conversión de texto a float y suma
numero = float('3.75') + 1
print(numero)  # Resultado: 4.75

# 4. Intercambiar valores sin tercera variable
x, y = 10, 20
x, y = y, x
print(f"x: {x}, y: {y}")