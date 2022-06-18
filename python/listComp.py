#!/usr/bin/env python3


import sys


def line():
    print("-" * 40)

def ex_1():
    """A Listaban levo szavakat csupa nagybetuve alakitja."""
    words = ['auto', 'villamos', 'metro']
    result = [w.upper() + '!' for w in words]
    print("Feladat 1:")
    print (words)
    print ("->")
    print (result)


def ex_2():
    """A Listaban levo szavakat kezdo nagybetuve alakitja."""
    words = ['aladar', 'bela', 'cecil']
    result = [w.capitalize() for w in words]
    print("Feladat 2:")
    print (words)
    print ("->")
    print (result)


def ex_3():
    """A fuggvény inicializál egy 10-elemu listát csupa 0-val"""
    result = [0 for i in range(10)]
    print("Feladat 3:")
    print(result)


def ex_4():
    """A fuggveny a listaban levo szamokat megszorozza 2-vel"""
    lst = list(range(1,10+1))
    result = [n*2 for n in lst]
    print("Feladat 4:")
    print (lst)
    print ("->")
    print (result)


def ex_5():
    """A fuggveny a listaban levo sztringeket szamma alakitja"""
    lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result = [int(i) for i in lst]
    print("Feladat 5:")
    print (lst)
    print ("->")
    print (result)


def ex_6():
    """A fuggveny a sztrigben levo szamot szamjegyenkent a listaba pakolja."""
    text = "1234567"
    result = [int(i) for i in text]
    print("Feladat 6:")
    print (text)
    print ("->")
    print (result)


def ex_7():
    """A fuggveny megallapítja az egyes szavak hosszat."""
    text = 'The quick brown fox jumps over the lazy dog'
    result = [len(word) for word in text.split()]
    print("Feladat 7:")
    print (text)
    print ("->")
    print (result)


def ex_8():
    """A fuggveny a sztring szavainak kezdobetujet egy listaba gyujti ossze."""
    text = "python is an awesome language"
    result = [list(i)[0] for i in text.split()]
    print("Feladat 8:")
    print (text)
    print ("->")
    print (result)


def ex_9():
    """A fuggveny a sztring szavait és annak hosszat tuple segitsegevel listaba gyujti."""
    text = 'The quick brown fox jumps over the lazy dog'
    result = [(i, len(i)) for i in text.split()]
    print("Feladat 9:")
    print (text)
    print ("->")
    print (result)


def ex_10():
    """A fuggveny 10-nel kisebb paros szamokbol allo listat allit elo."""
    result = [i for i in range(10) if i % 2 == 0]
    print("Feladat 10:")
    print (result)


def ex_11():
    """A fuggveny a 20-nal kisebb szamok negyzetet szamitja ki es a paros szamokat listaba gyujti."""
    result = [i*i for i in range(20) if i*i % 2 == 0]
    print("Feladat 11:")
    print (result)


def ex_12():
    """A fuggveny a 20-nal kisebb számok negyzetet allitja elő,
    majd a 4-el vegzodo szamokat listaba gyujti."""
    result = [i*i for i in range(20) if i*i % 2 == 0 and i*i % 10 == 4]
    print("Feladat 12:")
    print (result)


def ex_13():
    """Az angol abc nagybetuit listaba gyujti, majd egyetlen sztringge alakitja."""
    result = ""
    alphabet = [chr(i) for i in range(65,91)]
    result = result.join(alphabet)
    print("Feladat 13:")
    print (result)


def ex_14():
    """A fuggveny a listaban levo szavak elejerol es vegerol eltavolitja a whitespace karaktereket."""
    words = [' apple ', ' banana ', ' kiwi '] 
    result = [w.strip() for w in words]
    print("Feladat 14:")
    print (words)
    print ("->")
    print (result)


def ex_15():
    """A fuggveny a listaban levo szamjegyeket osszefuzi egy sztringge."""
    num_lst = [1, 0, 1, 1, 0, 1, 0, 0]
    str_lst = [str(i) for i in num_lst]
    result = str(''.join(str_lst))
    print("Feladat 15:")
    print (num_lst)
    print ("->")
    print (result)


def main():
    ex_1()
    line()
    ex_2()
    line()
    ex_3()
    line()
    ex_4()
    line()
    ex_5()
    line()
    ex_6()
    line()
    ex_7()
    line()
    ex_8()
    line()
    ex_9()
    line()
    ex_10()
    line()
    ex_11()
    line()
    ex_12()
    line()
    ex_13()
    line()
    ex_14()
    line()
    ex_15()
    line()


########################################

if __name__ == "__main__":
    main()