class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estás escuchando música")
telefono = FabricaTelefonos()
telefono.marca # Atributo
telefono.color # Atributo
telefono.memoriaRam # Atributo
telefono.almacenamiento # Atributo

print(telefono.llamar("Hola, ¿con quién hablo?"))
telefono.escucharMusica()