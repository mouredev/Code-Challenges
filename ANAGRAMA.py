import random

def is_Anagrama(word_1:str, word_2:str) -> bool:
    
    if word_1.lower() == word_2.lower():
        return False
    
    return "".join([c for c in sorted(word_2.lower())]) ==  "".join([c for c in sorted(word_1.lower())])
    


def main():
    print(is_Anagrama("dadlks", "dadlks"))



if __name__ == "__main__":
    main()

