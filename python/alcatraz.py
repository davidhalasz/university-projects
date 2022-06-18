#!/usr/bin/env python3

def helper(li, n):
    for c, i in enumerate(li,1):
        if c % n == 0:
            if li[c-1] == 0:
                li[c-1] = 1
            else:
                li[c-1] = 0
    return li


def main():
    li = []

    for i in range (1, 601):
        li.append(0)

    n = 1
    edited_list = []

    for i in li:
        edited_list = helper(li,n)
        n += 1
    
    result = []
    for c,i in enumerate(edited_list, 1):
        if i == 1:
            result.append(str(c))

    print(", ".join(result))    
       

############

if __name__ == "__main__":
    main()