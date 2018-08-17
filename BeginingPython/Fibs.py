# -*- coding: utf-8 -*-

class Fibs1:
    """
    循环
    """
    def __init__(self, n = 0):
        self.n = n

    def fib(self, n):
        result = [0, 1]
        for i in range(n-2):
            result.append(result[-2]+result[-1])
        return result


class Fibs2:
    """
    递归
    """
    def fibxxx(self, n):
        result = []
        if n == 1 or n == 0:
            result = 1
        else:
            result = self.fibxxx(n - 2) + self.fibxxx(n - 1)
        return result


class Fibs3:
    """
    迭代器
    """
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a+ self.b
        return self.a
    def __iter__(self):
        return self



    fib3 = Fibs3()
    for f in fib3:
        if f > 1000:
            print f
            break


if __name__ == '__main__':
    test()

# fib1 = Fibs1()
# print fib1.fib(15)

# fib2 = Fibs2()
# print fib2.fibxxx(13)
