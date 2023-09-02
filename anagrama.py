###
#* Reto #1
#* ¿ES UN ANAGRAMA?
#* Fecha publicación enunciado: 03/01/22
#* Fecha publicación resolución: 10/01/22
#* Dificultad: MEDIA
#*
#* Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#* Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#* NO hace falta comprobar que ambas palabras existan.
#* Dos palabras exactamente iguales no son anagrama.
#*
#* Información adicional:
#* - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#* - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

word1 = input("Ingrese una palabra: ")
word2 = input("Ingrese otra palabra: ")

def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        print(F"{word1} y {word2} son la misma palabra por lo que no es un anagrama.")
        return False 
    elif sorted(word1.lower()) == sorted(word2.lower()):
        print(F"La palabra {word1} y la palabra {word2}, son anagramas.")
        return True
    else:
        print(f"La palabra {word1} y la palabra {word2}, no son anagramas.")
        return False
    
print(is_anagram(word1, word2))


