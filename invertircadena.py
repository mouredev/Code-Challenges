"""Crea un programa que invierte el orden de una cadena de 
texto, sin usar las funciones propias del lenguaje que lo hagan de
forma automatica
- Si le pasamos Hola Mundo deberia retornar odnuM aloH"""
cadena2 = []

def invertir_cadena(cadena):
    invertido = ""
    for letra in cadena:
        cadena2.append(letra)
            
    for i in cadena2[::-1]:
        invertido += i
    print(invertido)

cadena = "Hola Mundo"
invertir_cadena(cadena)

def reverse(text):
    reversed_text = ""
    for index in range(0,len(text)):
        reversed_text = text[index] + reversed_text
    print(reversed_text)
reverse("Hola Mundo")

