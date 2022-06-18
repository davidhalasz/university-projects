#!/usr/bin/env python3

# Rekurzív módon eldönti, hogy egy adott szó palindróm-e.
def is_palindrome(s, start, end):
    if s[start] != s[end]:
        return False

    if start < (end+1):
        return is_palindrome(s, start+1, end-1)
    
    return True
    
    
def main():
    s = str(input("Adj meg egy szót: "))
    n = len(s)
    print("{0}: {1}".format(s, is_palindrome(s, 0, n-1)))

##############################################################################

if __name__ == "__main__":
    main()