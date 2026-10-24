# 1. Clase Aprendiz
class Aprendiz:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def mostrar_datos(self):
        print(f"Aprendiz: {self.nombre} | Ficha: {self.ficha}")

a1 = Aprendiz("Santiago Velásquez", "3311986")
a1.mostrar_datos()

# 2. Clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

r = Rectangulo(10, 4)
print(f"Área: {r.area()}, Perímetro: {r.perimetro()}")

# 3. Modificación a Cuenta (sin saldo negativo)
class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes.")

cuenta = Cuenta(1000)
cuenta.retirar(1200)  # Rechazado
cuenta.retirar(400)   # Aceptado

# 4. Herencia Vehiculo y Moto
class Vehiculo:
    def describir(self):
        print("Este es un vehículo general.")

class Moto(Vehiculo):
    def describir(self):
        print("Esta es una motocicleta de dos ruedas.")

m = Moto()
m.describir()