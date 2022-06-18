#!/usr/bin/env python3

def printDiamond(magassag):
    txt = "*"
    lst = []
    for i in range(1, magassag+1):
        if (i%2 == 1):
            csillag = i*txt
            lst.append(csillag.center(magassag, " "))
    
    cutted = lst[:-1]
    for e in cutted[::-1]:
        lst.append(e)

    return lst

def main():
    print("Magasság: 3")
    for e in printDiamond(3):
        print(e)
    
    print("\n\nMagasság: 7")
    for e in printDiamond(7):
        print(e)


##############################################################################

if __name__ == "__main__":
    main()