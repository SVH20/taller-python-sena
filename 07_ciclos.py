# Ejercicio 1: Pares del 1 al 50
for i in range(2, 51, 2):
    print(i, end=" ")
print()

# Ejercicio 2: Suma del 1 al 100
print("Suma del 1 al 100:", sum(range(1, 101)))

# Ejercicio 3: Tabla de multiplicar
num = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Ejercicio 4: Validación de clave con while
clave_correcta = "sena2026"
clave = ""
while clave != clave_correcta:
    clave = input("Ingresa la clave: ")
print("¡Acceso permitido!")