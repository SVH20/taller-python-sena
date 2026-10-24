# Ejercicio 1: Presentación con f-string
nombre, edad, ciudad = "Santiago", 23, "Cali"
print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

# Ejercicio 2: Precio con 2 decimales
precio = 1999.5
print(f"Precio: ${precio:.2f}")

# Ejercicio 3: Tabla del 7 con .format()
for i in range(1, 4):
    print("7 x {} = {}".format(i, 7 * i))

# Ejercicio 4: Ceros a la izquierda
n = 7
print(f"{n:03d}")