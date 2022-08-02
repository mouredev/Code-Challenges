inicio = 2024
fin = (inicio+(600*4))
for año in range(inicio, fin, 4):
    if año // 4 == año / 4 and año // 100 == año / 100:
        # año = str(año)
        print(año + " No es año bisiesto!")
    else:
        print(año)