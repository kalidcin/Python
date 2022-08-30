"""while True:
    try:
        num1 = int(input("Ingresa un número: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")"""

"""while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es:", edad)
        break
    except ValueError:
        print("Haz colocado un valor erroneo")"""

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es", edad)
        break
    except KeyboardInterrupt: # Al utilizar Ctrl + C
        print("\nHas cancelado la ejecución")
        break