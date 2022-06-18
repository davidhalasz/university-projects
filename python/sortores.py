#!/usr/bin/env python3
import sys
import random as r

UPTO = 100

def main():
    n = 0
    for i in range(UPTO):
        n += 1
        if(n < 10):
            print(r.randint(0, 9), end="")
        else:
            print(r.randint(0, 9), end="\n")
            n = 0
    

##############################################################################

if __name__ == "__main__":
    main()