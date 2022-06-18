#!/usr/bin/env python3

class Sor:

    def __init__(self):
        self.data = []

    def betesz(self, value):
        self.data.append(value)

    def meret(self):
        return len(self.data)

    def ures(self):
        if len(self.data) > 0:
            return False

    def kivesz(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        return "None"
    
    def __str__(self):
        str_lst = [str(e) for e in self.data]
        return  " ".join(str_lst)


def main():
    v = Sor()
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


if __name__ == "__main__":
    main()