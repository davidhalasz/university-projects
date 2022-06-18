#!/usr/bin/env python3

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2
    
    return True


def is_palindrom(n: int) -> bool:
    lst = list(str(n))
    reverse_lst = lst[::-1]

    if "".join(lst) == "".join(reverse_lst):
        return True
    else:
        return False


def next_prime(n: int) -> int:
    prime = n 
    foundPrime = False
    foundPalindrom = False
    
    while(not foundPrime and not foundPalindrom):
        if is_prime(prime) == True and is_palindrom(prime) == True:
            foundPrime = True
            foundPalindrom = True
        else: 
            prime += 1
    
    return prime


def main() -> None:
    inp = int(input("Adj meg egy egész számot: "))
    print(next_prime(inp))
    
    
if __name__ == "__main__":
    main()