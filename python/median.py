#!/usr/bin/env python3

def median(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)

    if length % 2 != 0:
        res = sorted_lst[length // 2]
    else:
        half = length // 2
        res = float((sorted_lst[half - 1] + sorted_lst[(half)]) / 2)
    
    return res

def main():
    lst1 = [3, 2, 1, 4, 5]
    lst2 = [1, 300, 2, 200, 1]
    lst3 = [3, 6, 20, 99, 10, 15]

    print("A " + str(lst1) + " medián értéke: " + str(median(lst1)))
    print("A " + str(lst2) + " medián értéke: " + str(median(lst2)))
    print("A " + str(lst3) + " medián értéke: " + str(median(lst3)))


##############################

if __name__ == "__main__":
    main()