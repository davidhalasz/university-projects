#!/usr/bin/env python3
import math

def is_palindrom(n: int) -> bool:
    lst = list(str(n))
    reverse_lst = lst[::-1]

    if "".join(lst) == "".join(reverse_lst):
        return True
    else:
        return False
    

def convertToBinary(n: int) -> int:
    number = n
    li = []
    
    while number != 0:
        if number % 2 == 0:
            li.append("0")
            number = math.floor(number/2)
        else:
            li.append("1")
            number = math.floor(number/2)
    li = li[::-1]
    return int("".join(li))

def isStartWithOne(n: int) -> bool:
    string = str(n)
    if string.startswith("1"):
        return True
    else:
        return False


def main() -> None:
    number = 1000000
    result = 0

    for n in range(1, number):
        if isStartWithOne(convertToBinary(n)):
            if is_palindrom(n) and is_palindrom(convertToBinary(n)):
                result += n
    print(result)
    

if __name__ == "__main__":
    main()