class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        print(mensaje)

telefono = FabricaTelefonos()
telefono.marca # Atributo
telefono.color # Atributo
telefono.memoriaRam # Atributo
telefono.almacenamiento # Atributo

telefono.llamar("Hola, ¿con quién hablo?")
