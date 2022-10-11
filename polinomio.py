def Triangulo(base:int, altura: int) -> int:
    return f"{base * altura / 2} area del Triangulo" 

def Rectagulo(base:int, altura: int) -> int:
    return f"{base * altura} area del Rectangulo" 

def Cuadrado(Lado: int) -> int:
    return f"{Lado**2} area del Cuadrado" 

def area(poligono) -> int:
    return print(poligono)

def main():
    area(Triangulo(3, 5))
    area(Cuadrado(7))
    area(Rectagulo(10, 4))
    
    
if __name__ == "__main__":
    main()
