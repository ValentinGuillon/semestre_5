





def is_premier(nb):
    for i in range(2, nb):
        if (nb % i) == 0:
            return False
    
    return True


def sum(n):
    res = 0

    for i in range(1, n):
        if is_premier(i):
            res += i


    return res


def main():
    n = 100

    print("Somme des nombres premiers de:")
    for i in range(1, n+1):
        print(f"1 à {i} = {sum(i)}")





main()
