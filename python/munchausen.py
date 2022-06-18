#!/usr/bin/env python3

def munchausen(n):
    """A fuggveny visszaadja Munchausen szamokat."""
    numbers = []
    num = 0
    for i in range(n):
        for d in str(i):
            if int(d) != 0:
                num += int(d) ** int(d)
        if i == num:
            numbers.append(i)
        num = 0
    return numbers


def main():
    #print('Az összes 10 000-nél kisebb Münchausen szám:')
    #print(munchausen(10000)) 
    print('Az összes Münchausen szám:')
    print(munchausen(440000000))   


########################

if __name__ == "__main__":
    main() 