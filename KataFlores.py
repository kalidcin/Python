def flores(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return print(True)
    elif flower1 % 2 != 0 and flower2 % 2 ==0:
        return print(True)
    else:
        return print(False)

flores(5, 5)