# 1. 5 ciudades de Colombia
ciudades = ["Cali", "Bogotá", "Medellín", "Barranquilla", "Cartagena"]
print("Primera:", ciudades[0], "| Última:", ciudades[-1])

# 2. Agregar dos ciudades y eliminar una
ciudades.append("Bucaramanga")
ciudades.append("Pereira")
ciudades.remove("Bogotá")
print(ciudades)

# 3. Ordenar números de mayor a menor
numeros = [15, 3, 89, 42, 7, 21]
numeros.sort(reverse=True)
print(numeros)

# 4. Suma, mayor y menor de una lista
datos = [10, 25, 5, 40, 18]
print(f"Suma: {sum(datos)}, Mayor: {max(datos)}, Menor: {min(datos)}")