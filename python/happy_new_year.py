#!/usr/bin/env python

def hpn():
    """A fuggveny szam hasznalata nelkul visszaadja, hogy ketezerhuszonegy."""
    lst = ["ab", "", "cd", "e"]
    num_lst = [len(word) for word in lst]
    res = int(''.join(str(i) for i in num_lst))
    
    return res


def main():
    print(hpn())


###############################x

if __name__ == "__main__":
    main()