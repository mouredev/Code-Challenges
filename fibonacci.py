#/*
#* Reto #2
#* LA SUCESIÓN DE FIBONACCI
#* Fecha publicación enunciado: 10/01/22
#* Fecha publicación resolución: 17/01/22
#* Dificultad: DIFÍCIL
#*
#* Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
#* La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
#* 0, 1, 1, 2, 3, 5, 8, 13...

num = [0, 1]



for i in range(51):
    fib = num[0 + i] + num[1 + i] 
    num.append(fib)        


for i in range(0,50):
    print(num[i])






def fibonacci():

    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(48):
        fib = n1 + n2
        n1 = n2
        n2 = fib
        print(fib)

fibonacci()

