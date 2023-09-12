
NB_CHAR_EXO1 = 29 #nb de characters possible
NB_CHAR_EXO2 = 26


#return a new dict with key and value swappped
def dict_inverser(dico: dict) -> dict:
    dico_return: dict = {}

    for key, value in dico.items():
        dico_return[value] = key

    return dico_return




def encode(dico, text: str) -> list[int]:
    ret = []
    for letter in text:
        ret.append(dico[letter])
    return ret


def decode(dico, text_to_decode: list[int]) -> str:
    dico = dict_inverser(dico)
    ret = ""
    for var in text_to_decode:
        ret += dico[var]
    return ret



#chiffre a message be replacing all character depending on the "key" (ex: if key=2, A->C)
def chiffre_cesar(dico, text, cle):
    text_e: list[int] = encode(dico, text)
    
    for i, val in enumerate(text_e):
        text_e[i] = (text_e[i] + cle) % NB_CHAR_EXO1

    ret = decode(dico, text_e)
    
    return ret

#dechiffre a message chiffred by cesar
def dechiffre_cesar(dico, text, cle):
    ret = chiffre_cesar(dico, text, (NB_CHAR_EXO1 - cle) % NB_CHAR_EXO1)
    return ret


#return the character with the most occurences in "text"
def plus_frequent(text: str) -> str:
    frequence = {}

    #on compte les occurences des char comme des débiles
    for letter in text:
        if not letter in frequence:
            frequence[letter] = 0
        frequence[letter] += 1

    #on cherche la plus grand
    most_frequent_char = "A"
    apparition = 0
    for key, value in frequence.items():
        if value > apparition:
            most_frequent_char = key
            apparition = value
        

    #print([(key, value) for key, value in frequence.items()])
    return most_frequent_char



#crack a message chiffred by cesar
def crack_cesar(dico: dict, text: str) -> str:
    #in the dico characters ensemble, the average most use character is the "space"
    #so, in a message chiffred by cesar, the char with the most occurence can be replace by the space
    
    most_appeared_char = plus_frequent(text)
    key = (dico[most_appeared_char] - dico[' ']) % NB_CHAR_EXO1
    cracked_text = dechiffre_cesar(dico, text, key)

    return cracked_text








def chiffre_affine(dico, text: str, cle_part_a, cle_part_b) -> str:
    #la permutation d'un char est donnée par la formule suivante: x -> ax + b (avec a =! 0)
    text_e: list[int] = encode(dico, text)
    
    for i, val in enumerate(text_e):
        text_e[i] = (cle_part_a * text_e[i] + cle_part_b) % NB_CHAR_EXO1

    ret = decode(dico, text_e)
    
    return ret


def dechiffre_affine(dico, text, cle_part_a, cle_part_b) -> str:
    text_e: list[int] = encode(dico, text)

    for i, val in enumerate(text_e):
        text_e[i] = (cle_part_a * text_e[i] + cle_part_b) % NB_CHAR_EXO1

    ret = decode(dico, text_e)

    return ret


def deux_plus_frequent(text: str) -> tuple[int]:
    first_most_frequent = plus_frequent(text)
    new_text = text.replace(first_most_frequent, '')
    second_most_frequent = plus_frequent(new_text)

    return first_most_frequent, second_most_frequent


def crack_affine(dico, text: str) -> str:
    #x : most frquent char,         y : frequency
    #x': second most frequent char, y': frequency
    #a = (y - y')((x - x')^-1)
    #b = y -ax

    first_char, second_char = deux_plus_frequent(text)
    frequence_first = frequence_second = 0
    for letter in text:
        if letter == first_char:
            frequence_first += 1
            continue
        if letter == second_char:
            frequence_second += 1

    print(f"first : {first_char} x{frequence_first}")
    print(f"second: {second_char} x{frequence_second}")

    a =       ((frequence_first - frequence_second)   * pow(   (dico[first_char] - dico[second_char])    , -1, 29)) % NB_CHAR_EXO1
    b = (frequence_first - (a * frequence_first)) % NB_CHAR_EXO1

    print(f"(a, b): {a}, {b}")

    cracked_text = dechiffre_affine(dico, text, a, b)
    return cracked_text








def chiffre_vigenere(dico, text: str, key: str) -> str:
    text_e: list[int] = encode(dico, text)
    key_e: list[int] = encode(dico, key)
    len_key = len(key)

    for i, letter in enumerate(text_e):
        text_e[i] = (letter + key_e[i % len_key]) % NB_CHAR_EXO2
    
    return decode(dico, text_e)


def dechiffre_vigenere(dico, text: str, key: str) -> str:
    key_e: list[int] = encode(dico, key)
    for i, val in enumerate(key_e):
        key_e[i] = (NB_CHAR_EXO2 - val) % NB_CHAR_EXO2
    new_key = decode(dico, key_e)

    dechiffred_message = chiffre_vigenere(dico, text, new_key)
    return dechiffred_message











def exo1():
    alpha: dict = {} #character as key, associate with a unique integer

    #fill alpha with caps alphabet and characters "space", "apostrophe" and "point"
    for i in range(26):
        alpha[chr(i+65)] = i
    alpha[" "] = 26
    alpha["'"] = 27
    alpha["."] = 28


    #ENCODE / DECODE
    print(f"\"ABCDEG\" -> encode -> {encode(alpha, 'ABCDEG')}")
    #must print "[0, 1, 2, 3, 4, 6]"
    print(f'"[15, 28, 25, 3]" -> decode -> {decode(alpha, [15, 28, 25, 3])}')
    #must print "P.ZD"

    print("\n")
    #CHIFFRE / DECHIFFRE CESAR

    message = "FAIT CHIER"
    cle = 5
    chiffre = chiffre_cesar(alpha, message, cle)
    dechiffre = dechiffre_cesar(alpha, chiffre, cle)
    print(f"message: {message}, key: {cle}")
    print(f'"{message}" -> chiffre cesar -> "{chiffre}" -> dechiffre cesar -> "{dechiffre}"')
    

    text_chiffred_by_cesar = ""

    with open("docs-tp0/affine/enc_cesar.txt", 'r') as file:
        for line in file:
            text_chiffred_by_cesar += line
        
    cracked_cesar = crack_cesar(alpha, text_chiffred_by_cesar)
    print("\nCrack of a message chiffred by cesar:\n", cracked_cesar)


    print("\n")
    #CHIFFRE / DECHIFFRE AFFINE
    print(f"\"INFORMATIQUE\" -> encode -> {chiffre_affine(alpha, 'INFORMATIQUE', 13, 12)}")
    #must print "AHTUBXM'ARLG"

    text_chiffred_by_affine = ""

    with open("docs-tp0/affine/enc_affine.txt", 'r') as file:
        for line in file:
            text_chiffred_by_affine += line
    
    
    cracked_affine = crack_affine(alpha, text_chiffred_by_affine)
    print("\nCrack of a message chiffred by affine:\n", cracked_affine)





def exo2():
    alpha: dict = {} #character as key, associate with a unique integer

    #fill alpha with caps alphabet
    for i in range(26):
        alpha[chr(i+65)] = i



    key = "CRYPTO"
    text_clear = "LECHIFFREMENTDEVIGENERE"

    print(f'"{text_clear}" -> chiffre vigenere -> "{chiffre_vigenere(alpha, text_clear, key)}"')
    #must print "NVAWBTHICBXBVUCKBUGECGX"

    text_chiffred = "NVAWBTHICBXBVUCKBUGECGX"
    print(f'"{text_chiffred}" -> dechiffre vigenere -> "{dechiffre_vigenere(alpha, text_chiffred, key)}"')
    #must print "NVAWBTHICBXBVUCKBUGECGX"



def main():
    # exo1()
    exo2()


if __name__ == "__main__":
    main()


