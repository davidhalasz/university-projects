#!/usr/bin/env python3

def main():
    parts = []
    for i in range(1, 100+1):
        parts.append(str(i))
    joinedList = "".join(parts)

    lst = list(joinedList)
    res = 0
    for i in lst:
        res += int(i)
    
    print("1-től 100-ig a számjegyek összege: ", res)


##############################################################################

if __name__ == "__main__":
    main()