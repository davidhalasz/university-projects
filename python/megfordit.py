#!/usr/bin/env python3

# megfordítja a bementül kapott számjegyeket.
def reverse(n):
    rn = str(n)[::-1]
    return int(rn)


def main():
    szam = int(input("Adj meg egy számot: "))

    print (reverse(szam))

##############################################################################

if __name__ == "__main__":
    main()