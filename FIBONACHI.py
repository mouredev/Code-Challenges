def fibonachi(cantidad_de_numros:int = 10 ) -> int:
    """
    - Retorna en la secuencia de fibonachi la cantidad de numeros que especiques.
    
    - Por defecto devuelve los 10 primeros.
    
    ### Ejemplo:
    
    >>> fibonachi(8)
    0, 1, 1, 2, 3, 5, 8, 13
    
    """
    numero_one = 0
    numero_two = 1
    
    iterador = 0
    
    while iterador < cantidad_de_numros:
        
        print(numero_one)
        
        numero_one, numero_two = numero_two, numero_one + numero_two
        
        iterador += 1



def main():
    fibonachi()



if __name__ == "__main__":
    main()