#!/usr/bin/env python3

#A szkript kiszámítja az első száz természetes szám összegének a négyzete és 
#az első száz természetes szám négyzetösszege közti különbséget!

def negyzetOsszeg(n):
    a = 0
    for i in range(0, n+1):
        a += i**2
    return int(a)


def osszegNegyzet(n):
    b = 0
    for i in range(0, n+1):
        b += i  
    
    return int(b**2)


def main():
    result = osszegNegyzet(100) - negyzetOsszeg(100)
    print("Az első száz természetes szám összegének a négyzete: ", osszegNegyzet(100))
    print("Az első száz természetes szám négyzetösszege: ", negyzetOsszeg(100))
    print("A két szám közti különbség: ", result )


if __name__ == "__main__":
    main()