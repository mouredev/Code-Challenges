def prime_numbers(numero):
    "Comprueba que un numero sea primo"

    if numero < 1:
        return False

    elif numero % 2 != 0:
        return [i for i in range(100) if i % 2 != 0 and i % 3 != 0 ]

    else:
        return  f"""
                ({numero}) no es un numeo primo.\n
                - Numeros primeros: 1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53...
                    """



def main():
    print(prime_numbers(8))



if __name__ == "__main__":
    main()