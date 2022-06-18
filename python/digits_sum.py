#!/usr/bin/env python3
# coding: utf-8


def osszeg(num):
    str_digits = list(str(num))
    res = 0
    int_digits = []
    for i in str_digits:
        int_digits.append(int(i))
        
    return sum(int_digits)


def main():
    n = 2**1000
    print("A számjegyek összege:")
    print(osszeg(n))
    

##############################################################################

if __name__ == "__main__":
    main()