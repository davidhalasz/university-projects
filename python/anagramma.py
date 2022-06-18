#!/usr/bin/env python3
# coding: utf-8


def normalize(w):
    """A függvény visszaadja a sztring normalizált alakját.""" 
    return "".join(w.lower().split())


def anagramma(word1, word2):
    d1 = {}
    d2 = {}

    letters1 = list(normalize(word1))
    letters2 = list(normalize(word2))
    for l in letters1:
        if l not in d1:
            d1[l] = 1
        else:
            d1[l] += 1
    
    for l in letters2:
        if l not in d2:
            d2[l] = 1
        else:
            d2[l] += 1

    for k1, v1 in sorted(d1.items()):
        anagramma = True
        if k1 not in sorted(d2.keys()) or k1 in sorted(d2.keys()) and v1 != d2[k1]:
            anagramma = False
            break
    
    return anagramma            

def main():
    inp1 = str(input("Első szó: "))
    inp2 = str(input("Második szó: "))
    if anagramma(inp1, inp2):
        print("Ez a szó anagramma")
    else:
        print("Nem anagramma") 


##############################

if __name__ == "__main__":
    main()

