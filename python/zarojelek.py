#!/usr/bin/env python3

def check(txt):
    lst_txt = list(txt)
    open_lst = ["(", "{", "["]
    close_lst = [")", "}", "]"]
    op_dict = dict(zip(close_lst, open_lst))
    lst_op = []

    for s in lst_txt:
        if s in open_lst:
            lst_op.append(s)
        if s in close_lst:
            if lst_op[-1] == op_dict[s]:
                lst_op.pop()
            else:
                return False
    
    if len(lst_op) == 0:
        return True
    else:
        return False

def main():
    txt1 = "((5+3)*2+1)"
    txt2 = "{[(3+1)+2]+}"
    txt3 = "(3+{1-1)}"
    txt4 = "[1+1]+(2*2)-{3/3}"
    txt5 = "(({[(((1)-2)+3)-3]/3}-3)"
    print(txt1, check(txt1))
    print(txt2, check(txt2))
    print(txt3, check(txt3))
    print(txt4, check(txt4))
    print(txt5, check(txt5))

##############################################################################

if __name__ == "__main__":
    main()