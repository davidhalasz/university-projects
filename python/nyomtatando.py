#!/usr/bin/env python3

from typing import List

def pages_to_print(s: str) -> List[int]:
    pages = []
    li = s.split(",")
    for s in li:
        if "-" in s:
            nums = s.split("-")
            lst = range(int(nums[0]), (int(nums[1])+1))
            for n in lst:
                pages.append(n)
        else: 
            pages.append(int(s))

    return pages


def main() -> None:
    inp = input("Add meg a nyomtatandó oldalakat: ")
    print(pages_to_print(inp))



if __name__ == "__main__":
    main()