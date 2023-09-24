
NB_CHAR_EXO1 = 29 #nb de characters possible
NB_CHAR_EXO2 = 26


#return a new dict with key and value swappped
def dict_inverser(dico: dict) -> dict:
    dico_return: dict = {}

    for key, value in dico.items():
        dico_return[value] = key

    return dico_return


def char_frequency(c: str, text: str) -> int:
    frequency = 0

    for letter in text:
        if letter == c:
            frequency += 1

    return frequency





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



def calcule_decalage(dico: dict, text: str, char_averagely_most_present: str) -> int:
    most_appeared_char = plus_frequent(text)
    return (dico[most_appeared_char] - dico[char_averagely_most_present]) % NB_CHAR_EXO1


#crack a message chiffred by cesar
def crack_cesar(dico: dict, text: str) -> str:
    #in the dico characters ensemble, the average most use character is the "space"
    #so, in a message chiffred by cesar, the char with the most occurence can be replace by the space
    
    key = calcule_decalage(dico, text, ' ')
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
    frequence_first = char_frequency(first_char, text)
    frequence_second = char_frequency(second_char, text)

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



def ic(dico: dict, text: str) -> str:
    
    numerator = 0
    denominator = 0

    denominator = len(text) * (len(text) - 1 )

    for letter in list(dico.keys()):
        frequency = char_frequency(letter, text)
        numerator += frequency * (frequency - 1)
    
    return numerator / denominator

    # res = 0

    # denominator = len(text) * (len(text) - 1 )

    # for letter in list(dico.keys()):
    #     frequency = char_frequency(letter, text)
    #     res += (frequency * (frequency - 1)) / denominator
    
    # return res


#return the text with all char at index 0 and "len_crop" multiple
def crop_text(text: str, len_crop: int, start: int) -> str:
    new_text = ""
    i = start
    while i < len(text):
        new_text += text[i]
        i += len_crop
    
    return new_text




def calcule_longueur_cle(dico: dict, text: str) -> str:
    i_c = 0
    len_key = 0

    while i_c < 0.075:
        len_key += 1

        new_text = crop_text(text, len_key, 0)
        # i = 0
        # while i < len(text):
        #     new_text += text[i]
        #     i += len_key
        
        i_c = ic(dico, new_text)
        # print("ic =", i_c)
    
    print("ic =", i_c)
    return len_key





def crack_vigenere(dico: dict, text: str) -> str:
    print("\n!!! crack_vigenere() donne ne donne pas le bon résultat !!!")
    # text_e = encode(dico, text)

    len_key = calcule_longueur_cle(dico, text)
    key_encoded = []


    for i in range(len_key):
        temp_text = crop_text(text, len_key, i)
        decalage = calcule_decalage(dico, temp_text, 'E')
        key_encoded.append(decalage)
    
    key: str = decode(dico, key_encoded)
    print("key? = ", key)

    return dechiffre_vigenere(dico, text, key)














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


    texts_encrypted: list[str] = []

    for i in range(4):
        text = ""
        with open(f"docs-tp0/vigenere/file{i}_encrypted.txt", 'r') as file:
            for line in file:
                text += line
        
        texts_encrypted.append(text)


    print(ic(alpha, texts_encrypted[0]))

    # for i in range(4):
    #     print(f"text {i}, len key ? = ", calcule_longueur_cle(alpha, texts_encrypted[i]))

    print("\nCrack of a message chiffred by vigenere:")
    print(crack_vigenere(alpha, texts_encrypted[0]))





def main():
    exo1()
    print("\n!! formule du crackage du chiffrement affine incorrect !!\n")
    exo2()


if __name__ == "__main__":
    main()


