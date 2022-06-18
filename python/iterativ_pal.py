#!/usr/bin/env python3

# Iteratív módon eldönti egy sztringről, hogy palindróm-e.
def is_palindrome(s):
    ls = len(s)
    half = ls//2
    
    for i in s[0:half]:
        j = 0
        if s[j] != s[ls-j-1]:
            return False
        j += 1
    return True

    
def main():
    s = str(input("Adj meg egy szót: "))
    print("{0}: {1}".format(s, is_palindrome(s)))

##############################################################################

if __name__ == "__main__":
    main()