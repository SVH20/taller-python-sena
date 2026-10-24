# Ejercicio 1: Longitud de palabra
palabra = input("Ingresa una palabra: ")
print(f"Cantidad de caracteres: {len(palabra)}")

# Ejercicio 2: Quitar espacios y mayúsculas
frase = ' hola mundo '
print(frase.strip().upper())

# Ejercicio 3: Contar apariciones de 'a'
texto = "La programación en Python es apasionante"
print(f"Apariciones de la letra 'a': {texto.lower().count('a')}")

# Ejercicio 4: Invertir y palíndromo
cadena = "reconocer"
invertida = cadena[::-1]
print(f"Invertida: {invertida} | ¿Es palíndromo?: {cadena.lower() == invertida.lower()}")