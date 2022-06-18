#!/usr/bin/env python3

class MyQueue:

    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def size(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True

    def popleft(self):
        if len(self.data) > 0:
            x_lst = []

            for i in range(len(self.data)-1):
                x_lst.append(self.data.pop())

            res = self.data.pop()

            for i in range(len(x_lst)):
                self.data.append(x_lst.pop())

            return res
            #self.data = self.data[::-1]
            #x = self.data.pop()
            #self.data = self.data[::-1]
            #return x
        return "None"
    
    def __str__(self):
        str_lst = [str(e) for e in self.data]
        return " ".join(str_lst)


def main():
    q = MyQueue()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print("Teljes sor:", q)
    print("Kivett első elem:", q.popleft())
    print("Módosított sor:", q)
    print("Sor mérete:", q.size())
    print("Üres-e a sor?", q.is_empty())
    print("Kivett első elem:", q.popleft())
    print("Kivett első elem:", q.popleft())
    print("Kivett első elem:", q.popleft())
    print("Kivett első elem:", q.popleft())
    print("Üres-e a sor?", q.is_empty())

if __name__ == "__main__":
    main()