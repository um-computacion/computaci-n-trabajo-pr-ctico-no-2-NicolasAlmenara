def is_palindrome (word):
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace("'","")
    word = word.replace(",","")
    word = word.replace(":", "")
    word = word.replace("?", "")
    word = word.replace("¿", "")
    word = word.replace(".", "")
    word = word.replace("¡", "")
    word = word.replace("!", "")
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True


def main():
    repeat = "y"
    while repeat == "y":
        word = str(input("Ingrese la palabra o frase. "))
        result = is_palindrome(word)
        if result == True:
            print(f"{word} es un palindromo")
        else:
            print(f"{word} no es un palindromo")
        repeat = str(input("¿Desea ingresar otra palabra? y/n: ")).lower()

if __name__ == "__main__":
    main()