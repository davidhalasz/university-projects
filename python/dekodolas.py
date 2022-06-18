#!/usr/bin/env python3

# Rejtélyes üzenet feladat megoldása

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

def dekodolas(txt):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]    
    result = ""

    for t in txt:
        if t.isupper():
            t = t.lower()    
            if t in abc:
                n = abc.index(t)
                if n == 25:
                    n = 1
                if n == 24:
                    n = 0
                else:
                    n += 2
                result += abc[n].upper()
            else:
                result += t
        else:
            if t in abc:
                n = abc.index(t)
                if n == 25:
                    n = 1
                if n == 24:
                    n = 0
                else:
                    n += 2
                result += abc[n]
            else:
                result += t
    return result
    

def main():
    print(dekodolas(TEXT))

##############################################################################

if __name__ == "__main__":
    main()