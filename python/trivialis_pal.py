#!/usr/bin/env python3

# Triviális módszerrel eldönti, hogy egy sztring palindróm-e.
def is_palindrome(text):
    if text.lower()  == text[::-1].lower():
        return True
    return False

def main():
    s = str(input("Írj be egy szót, hogy kiderüljön, palindróm-e: "))
    print("{0}: {1}".format(s, is_palindrome(s)))

##############################################################################

if __name__ == "__main__":
    main()