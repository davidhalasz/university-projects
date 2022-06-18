#!/usr/bin/env python3

import sys

def list_sum():
    """A fuggveny kiszamitja az ezernel kisebb szamok osszeget, melyek 3-nak vagy 5-nek tobbszorosei."""
    res = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    print (res)


def main():
    list_sum()


########################

if __name__ == "__main__":
    main()