


#XOR between "l1" and "l2"
def permutation(l1: list[int], l2: list[int]) -> list[int]:
    for i in range(4):
        if l1[i] == l2[i]:
            l1[i] = 0
        else:
            l1[i] = 1
    
    return l1

def substitution(text: list[int]):
    res = [0 for x in range(4)]

    for i in range(4):
        j = (16 * i) % 4
        res[j] = text[i]
    
    return res



def round(text: list[int], key: list[int]) -> list[int]:
    print("texte before:", text)
    text = permutation(text, key)
    text = substitution(text)
    print("texte after:", text)
    return text



def enc(text: list[int], key: list[int]) -> list[int]:
    for i in range(4):
        print(f"r{i}:")
        text = round(text, key)
    return text



def exo1():
    text = [0, 1, 1, 0]
    key = [1, 1, 0, 1]
    chiffre = enc(text, key)
    print(chiffre)




def main():
    exo1()


if __name__ == "__main__":
    main()
