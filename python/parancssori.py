#!/usr/bin/env python3
import sys

def osszeg(nums):
    if(len(nums) == 2):
        num1 = int(nums[0])
        num2 = int(nums[1])
        print("A két szám összege: ", num1+num2)
    elif(len(nums) < 2):
        print("Hiba! Nincs megadva mindkét szám!")
    else:
        print("Hiba! Több, mint két szám van megadva!")


def main():
    osszeg(sys.argv[1:])
    

##############################################################################

if __name__ == "__main__":
    main()