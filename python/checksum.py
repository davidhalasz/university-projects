#!/usr/bin/env python3

class Checksum:
    
    def __init__(self):
        self.result = 0
    
    def find_a(self, value):
        sorted_lst = sorted(value)
        a = (sorted_lst[::-1]).pop()
        return a

    def find_b(self, value):
        sorted_lst = sorted(value)
        b = sorted_lst.pop()
        return b

    def diff_ab(self, v_a, v_b):
        self.result += (v_b - v_a)

    def __str__(self):
        return str(self.result)



def main():
    with open('input.txt', 'r') as f:
        l = [[int(num) for num in line.split('\t')] for line in f]
    
    ch = Checksum()
    for i in l:
        ra = ch.find_a(i)
        rb = ch.find_b(i)
        ch.diff_ab(ra, rb)
    print(ch)

if __name__ == "__main__":
    main()