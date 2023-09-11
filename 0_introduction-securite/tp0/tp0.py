
NB_CHAR = 29 #nb de characters possible



def encode(dico, text: str) -> list[int]:
    ret = []
    for letter in text:
        ret.append(dico[letter])
    return ret

def decode(dico, text_to_decode: list[int]) -> str:
    ret = ""
    for var in text_to_decode:
        ret += dico[var]
    return ret


def chiffre_cesar(dico, dico_inv, text, cle):
    text_e: list[int] = encode(dico, text)
    
    for i, val in enumerate(text_e):
        text_e[i] = (text_e[i] + cle) % NB_CHAR

    ret = decode(dico_inv, text_e)
    
    return ret


def dechiffre_cesar(dico, dico_inv, text, cle):
    ret = chiffre_cesar(dico, dico_inv, text, (NB_CHAR - cle) % NB_CHAR)
    return ret




def plus_frequent(dico, text: str) -> str:
    #allow_chars = 
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





def chiffre_affine(dico, dico_inv, text, cle_a, cle_b) -> str:
    text_e: list[int] = encode(dico, text)
    
    for i, val in enumerate(text_e):
        text_e[i] = (cle_a * text_e[i] + cle_b) % NB_CHAR

    ret = decode(dico_inv, text_e)
    
    return ret




def dechiffre_affine(dico, dico_inv, text, cle_a, cle_b) -> str:
    text_e: list[int] = encode(dico, text)
    
    
    for i, val in enumerate(text_e):
        text_e[i] = (cle_a * text_e[i] + cle_b) % NB_CHAR

    ret = decode(dico_inv, text_e)
    
    return ret


def deux_plus_frequent(dico, text: str) -> tuple[int]:
    #allow_chars = 
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
            
    #on cherche la deuxieme plus grand
    most_frequent_char_2 = "A"
    apparition_2 = 0
    for key, value in frequence.items():
        if value > apparition:
            most_frequent_char = key
            apparition = value
        

    #print([(key, value) for key, value in frequence.items()])
    return most_frequent_char, most_frequent_char_2









def main():
    alpha = {}
    alpha_inv = {}

    #fill alpha with caps alphabet and 
    #ALPHA
    for i in range(26):
        alpha[chr(i+65)] = i
    alpha[" "] = 26
    alpha["'"] = 27
    alpha["."] = 28

    #ALPHA inversé
    for key, value in alpha.items():
        alpha_inv[value] = key



    #for key, value in alpha.items():
    #    print (key, value)
    #for key, value in alpha_inv.items():
    #    print (key, value)
    


    
    print(encode(alpha, "ABCDEG"))
    print(decode(alpha_inv, [0, 12, 25, 28]))
    
    mot_test = "FAIT CHIER"
    cle = 5
    test_1 = chiffre_cesar(alpha, alpha_inv, mot_test, cle)
    test_2 = dechiffre_cesar(alpha, alpha_inv, test_1, cle)
    print(test_1, test_2)
    


    a = plus_frequent(alpha, "aabbccc")
    print(a)

    b = "HQLJPDAFKLIIUHAOHVALQIRUPDWLRQVAHQAIDLVDQWASDVVHUAXQAFRXUDQWAHOHFWULTXHADAWUDYHUVAXQHAVHULHAGHAFRPSRVDQWVCAFHAFRXUDQWAHVWAWUDQVPLVAHQASUHVVDQWAXQHAOHWWUHAVXUAOHAFODYLHUAALOAWUDYHUVHAXQAUHVHDXAFRPSOHHAGHAILOVASXLVADOOXPHAXQHAODPSHATXLALQGLTXHAODAOHWWUHAFKLIIUHHCAOHASUHPLHUAFRPSRVDQWAGXAUHVHDXAHVWAXQHAVHULHAGHAURXHVADGMDFHQWHVADSSHOHHVAAURWRUVAATXLAFRQWLHQQHQWAOHVAILOVAHOHFWULTXHVAXWLOLVHVASRXUAFKLIIUHUAOHAPHVVDJHCAOHVAURWRUVAWRXUQHQWAPRGLILDQWAODAFRQILJXUDWLRQAFRPSOH HAGXAUHVHDXAFKDTXHAIRLVATXBXQHAOHWWUHAHVWAWDSHHCAHQLJPDAXWLOLVHAKDELWXHOOHPHQWAXQHADXWUHAURXHADSSHOHHAAUHIOHFWHXUAAHWAXQAFRPSRVDQWADSSHOHAAWDEOHDXAGHAFRQQH LRQAAFHATXLASHUPHWAGHAUHQGUHASOXVAFRPSOH HAHQFRUHAOHASURFHVVXVAGHAFKLIIUHPHQWC"


    
    c = plus_frequent(alpha, b)
    print(c)
    decalage = (alpha[c] - alpha[' ']) % NB_CHAR
    
    
    b_dechiffre = dechiffre_cesar(alpha, alpha_inv, b, decalage)
    print(b_dechiffre)
    
    
    
    
    
    
    e = deux_plus_frequent(dico, text: str) -> tuple[int]:
    
    
    






if __name__ == "__main__":
    main()


