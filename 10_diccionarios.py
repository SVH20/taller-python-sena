# Ejercicio 1: Datos de un libro
libro = {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967}
print(libro)

# Ejercicio 2: Precios y total
productos = {"Arroz": 3500, "Leche": 4200, "Huevos": 16000, "Café": 8500}
print(f"Total productos: ${sum(productos.values())}")

# Ejercicio 3: Traductor
traducciones = {"hola": "hello", "mundo": "world", "python": "python"}
palabra = input("Palabra en español: ").lower()
print("Traducción:", traducciones.get(palabra, "No encontrada"))

# Ejercicio 4: Conteo de palabras
frase = "python es genial y aprender python es divertido"
conteo = {}
for p in frase.split():
    conteo[p] = conteo.get(p, 0) + 1
print(conteo)