"""class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self):
        self.marca = "Huawei"

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)"""

"""class FabricaTelefonos():
    def __init__(self): # Se ejecuta al crear un objeto de esta clase
        print("Estoy ejecutando el metodo Init, porque se ha creado un nuevo objeto")

telefono = FabricaTelefonos() # Creación del objeto
telefono2 = FabricaTelefonos()"""

class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca # Iguala los atributos a las variables globales
        self.color = color # Iguala los atributos a las variables globales

telefono = FabricaTelefonos('Huawei', 'Azul')
print(telefono.marca)
print(telefono.color)   