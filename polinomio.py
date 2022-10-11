presentacion = """

|*****************************************************************|
|    Hola!, si esta aqui es porque esta interesado en aprender.   |
|---------------------------------------------------------------- | 
|   		¿De que poligono te gustaria saber su area?.          |
|-----------------------------------------------------------------|
|																  |
|	           	1. Triangulo 									  |
|      	        2. Cuadrado										  |
|        	    3. Rectangulo								      |
|																  |
|																  |
|-----------------------------------------------------------------|
    """
    
def area():
	"""
	"""
	print(presentacion)
 
	opcion = int(input("Opcion: "))
 
	if opcion == 1:
		base = int(input("Elige lan la Base y altur.\n  Base: "))
		altura = int(input("Altura: "))
		return print(f" area {base * altura / 2} del Triangulo")

	elif opcion == 2:
		altura = int(input("Elige lan la Base y altur.\n  altura: "))
		return  print(f" area {altura**2} del Cuadrado")

	elif opcion == 3:
		base = int(input("Elige lan la Base y altur.\n  Base: "))
		altura = int(input("Altura: "))
		return  print(f" area {base * altura } del Rectangulo")

	else: 
		print(f"({opcion}) no exite :(")

def main():
	area()



if __name__ == "__main__":
    main()
