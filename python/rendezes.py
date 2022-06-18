#!/usr/bin/env python3

# def my_func1(t):
    # return t[-1]


# def my_func2(user):
    # return int(user.split(":")[0])


# def my_func3(l):
    # return l[1]


def main():
    # Feladat 1:
    data = [ 
        (1,'Albany','NY',162692),
        (3,'Allegany','NY',11986),
        (121,'Wyoming','NY',8722),
        (123,'Yates','NY',5094)
    ]
    print("Feladat 1:")
    print(sorted(data, key=lambda t: t[-1]))
    print("\n")

    # Feladat 2:
    lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print("Feladat 2:")
    print(sorted(lst, key=lambda user: int(user.split(":")[0]), reverse=True))
    print("\n")

    # Feladat 3:
    li = [ [2,6],[1,3],[5,4] ]
    print("Feladat 3:")
    print(sorted(li, key=lambda x: x[1]))

if __name__ == "__main__":
    main()