#!/usr/bin/env python3


def main():
    alphabet = [chr(c) for c in range(97, 123)]
    res = ''.join(alphabet[::-1])
    print (res)


###############################x

if __name__ == "__main__":
    main()