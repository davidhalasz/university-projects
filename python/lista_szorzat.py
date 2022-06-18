#!/usr/bin/env python3

# A listában lévő elemek szorzatát számítja ki.
def szorzas(li):
    res = 1
    for n in li:
       res = res * n
    return res


def main():
    li = [1, 5, 15, 8]
    emptyLi = []

    print ("[1, 5, 15, 8] esetén az eredmény: ", szorzas(li))
    print ("Üres lista esetén: ", szorzas(emptyLi))

##############################################################################

if __name__ == "__main__":
    main()