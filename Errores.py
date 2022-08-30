while True:
    try: # El codigo que vigilará si tiene errores
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es:", edad)
        break # Termina la ejecución si no entra en el Except
    except: # Imprime esto si pones Str, Bool, etc
        print("Ingresaste un valor erroneo")
    finally: # Siempre se ejecuta
        print("La ejecución ha finalizado")