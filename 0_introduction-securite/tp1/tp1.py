



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
    # print("l1:", l1)
    # print("l2:", l2)
    return [l1[i] ^ l2[i] for i in range(4)]


def substitution(text: list[int]):
    res = [0 for _ in range(4)]

    for i in range(4):
        j = (i + 2) % 4
        res[j] = text[i]
    
    return res

def anti_substitution(text: list[int]):
    res = [0 for _ in range(4)]

    for i in range(4):
        j = (i - 2) % 4
        res[j] = text[i]
    
    return res




def round(text: list[int], key: list[int]) -> list[int]:
    # print("text before :", *text)
    text = permutation(text, key)
    # print("text permute:", *text)
    text = substitution(text)
    # print("text substi :", *text)
    return text


def back_round(text: list[int], key: list[int]) -> list[int]:
    text = anti_substitution(text)
    text = permutation(text, key)
    return text


def enc(text: list[int], key: list[int]) -> list[int]:

    text_s = split_text(text, 4)
    key_s = split_text(key, 4)
    res: list[list[int]] = []


    for i, part in enumerate(text_s):
        # sub_key = key[(i*4) % len(key): ((i*4)+4) % len(key)]
        sub_key = key_s[i % (len(key_s))]
        # print("sub_key = ", *sub_key)
        res.append(round(part, sub_key))

    return unsplit_text(res)


def dec(text: list[int], key: list[int]) -> list[int]:

    text_s = split_text(text, 4)
    key_s = split_text(key, 4)
    res: list[list[int]] = []


    for i, part in enumerate(text_s):
        # sub_key = key[(i*4) % len(key): ((i*4)+4) % (len(key) - 1)]
        sub_key = key_s[i % (len(key_s))]
        # print("sub_key = ", *sub_key)
        res.append(back_round(part, sub_key))

    return unsplit_text(res)




def fill_to_eight(text: str) -> str:
    while(len(text) < 8):
        text = '0' + text
    return text

def enc_byte(text: str) -> list[int]:
    res: str = ""

    for character in text:
        res += fill_to_eight(bin(ord(character))[2:])
    
    return [int(x) for x in res]


def dec_byte(text: list[int]) -> str:
    res = ""

    for i in range(len(text) // 8):
        part = text[i*8: (i*8) + 8]
        part = ''.join(str(x) for x in part)
        res += chr(int(part, 2))
    
    return res






def exo1():
    print("!!! substitution() is veeeery simple !!!")
    text = [0, 1, 1, 0, 0, 0, 1, 0]
    key = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    print("text clear    :", *text)
    chiffre = enc(text, key)
    print("text chiffred :", *chiffre)
    print(*dec(chiffre, key))

    t = [1, 0, 0, 1, 1, 1, 0, 0]
    print(t)
    print(dec(enc(t, key), key))


def exo2():
    key = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]

    text: str = "Je galère, aled."
    a = enc_byte(text)
    print("a:", a)
    b = enc(a, key)
    print(b)
    print(dec_byte(b))
    c = dec(b, key)
    print(c)
    print(dec_byte(c))





def main():
    print("===========exo 1============")
    exo1()
    print("===========exo 2============")
    exo2()


if __name__ == "__main__":
    main()
