def organiza_numeros():
    
    """
    Eata funcione escriben FIZZ sin son divisible por 3
    y BUZZ sin son por 5, y si es por los dos FIZZ BUZZ
    
    >>> orgazina_numero()
    .... 1, 2, 3 FIZZ, 4, 5 BUZZ, 
    
    """
    
    for numero in range(1, 100):
        
        if (numero % 3 == 0 and numero % 5 == 0 ):
            print(f"{numero} FIZZ BUZZ ")
            
        elif numero % 3 == 0:
            print(f"{numero} FIZZ ")
            
        elif numero % 5 == 0:
            print(f"{numero} BUZZ")
            
        else:
            print(numero)
            


def run():
    organiza_numeros() 


if __name__ == "__main__":
    run()
    