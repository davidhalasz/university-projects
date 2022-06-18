#!/usr/bin/env python3
# coding: utf-8

def print_board(lst):

    board = [["."]*8 for i in range(8)]
    d = {
        0: 7,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1,
        7: 0 
    }

    for i in range(8):
        n = lst[i]
        get_d = d.get(n)
        board[get_d][i] = "Q"

    print("+" + "-"*17 + "+")  
    for i in range(8):
        print('| ' + " ".join(board[i]) + " |")  
    print("+" + "-"*17 + "+")


def main():
    lst = [0,4,7,5,2,6,1,3]
    print_board(lst)



##############################

if __name__ == "__main__":
    main()