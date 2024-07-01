class Desayuno:
    def __init__(self, nombre, ingredientes, fruta, postre, jugo):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.fruta = fruta
        self.postre = postre
        self.jugo = jugo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Ingredientes: {', '.join(self.ingredientes)}")
        print(f"Fruta fresca: {', '.join(self.fruta)}")
        print(f"Postre: {self.postre}")
        print(f"Bebida: {self.jugo}")

class Ordenes:
    def __init__(self):
        self.platillos_list = []

    def agregar_platillo(self, platillo):
        self.platillos_list.append(platillo)

    def calcular_total(self):
        total = sum(platillo.precio for platillo in self.platillos_list)
        print(f"Total de la orden: ${total:.2f}")

# Crear objetos
desayuno1 = Desayuno("Desayuno Americano", ["huevos", "tocino", "pan"], ["fresas", "manzana", "uvas"], "Flan de chocolate", "Jugo de naranja")
orden1 = Ordenes()
orden1.agregar_platillo(desayuno1)
orden1.calcular_total()