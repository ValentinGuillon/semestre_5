



def split_text(text: list[int], len_split: int) -> list[list[int]]:
    text_s: list[list[int]] = []

    temp: list[int] = []

    for i, value in enumerate(text, start= 1):
        temp.append(value)

        if i % len_split == 0:
            text_s.append(temp.copy())
            temp.clear()

    return text_s


def unsplit_text(text_splitted: list[list[int]]) -> list[int]:
    return [x for part in text_splitted for x in part]


#XOR between "l1" and "l2"
def permutation(l1: list[int], l2: list[int]) -> list[int]:
    for i in range(4):
        if l1[i] == l2[i]:
            l1[i] = 0
        else:
            l1[i] = 1
    
    return l1

def substitution(text: list[int]):
    res = [0 for _ in range(4)]

    for i in range(4):
        j = (4 * i) % 4
        res[j] = text[i]
    
    return res



def round(text: list[int], key: list[int]) -> list[int]:
    print("texte before:", *text)
    text = permutation(text, key)
    print("text mid    :", *text)
    # text = substitution(text)
    print("texte after :", *text)
    return text



def enc(text: list[int], key: list[int]) -> list[int]:

    text_s = split_text(text, 4)
    text_us = unsplit_text(text_s)
    res: list[list[int]] = []


    for i, part in enumerate(text_s):
        sub_key = key[(i*4) % len(key): ((i*4)+4) % len(key)]
        print("sub_key = ", *sub_key)
        res.append(round(part, sub_key))

    return unsplit_text(res)



def exo1():
    print("!!! substitution() won't called !!!")
    text = [0, 1, 1, 0, 0, 0, 1, 0]
    key = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    print("start:", *text)
    chiffre = enc(text, key)
    print("end:", *chiffre)




def main():
    exo1()


if __name__ == "__main__":
    main()
