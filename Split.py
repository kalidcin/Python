from posixpath import split


def stringSplit(s):
    lista = []
    lista.append(s.split())
    print(lista)

s = str(input("Escribe una frase: "))
stringSplit(s)
