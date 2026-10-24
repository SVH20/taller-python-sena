# Ejercicio 1: Operaciones básicas
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
print(f"Suma: {n1+n2} | Resta: {n1-n2} | Mult: {n1*n2} | Div: {n1/n2 if n2!=0 else 'N/A'}")

# Ejercicio 2: Guardar aprendiz en archivo
nombre = input("Nombre aprendiz: ")
ficha = input("Número ficha: ")
with open("registro.txt", "w", encoding="utf-8") as f:
    f.write(f"Nombre: {nombre}\nFicha: {ficha}\n")

# Ejercicio 3: Leer registro.txt
print("\n--- Contenido de registro.txt ---")
with open("registro.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())

# Ejercicio 4: Guardar notas y estado
n1 = float(input("\nNota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
prom = (n1 + n2 + n3) / 3
estado = "Aprobó" if prom >= 3.0 else "No aprobó"

with open("resultado.txt", "w", encoding="utf-8") as f:
    f.write(f"Promedio: {prom:.2f} - Estado: {estado}\n")
print(f"Resultado guardado: Promedio {prom:.2f} ({estado})")