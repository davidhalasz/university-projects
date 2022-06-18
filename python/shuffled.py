#!/usr/bin/env python3
import random
from typing import List 

def shuffled(li: List[int]) -> List[int]:
    inp_li = li
    random.shuffle(inp_li)
    return inp_li


def main() -> None:
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Input: ", lst)
    print("Összekevert lista utolsó eleme: ", shuffled(lst)[-1])


if __name__ == "__main__":
    main()