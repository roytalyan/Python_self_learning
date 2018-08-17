# -*- coding: utf-8 -*-


class Stack:
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

"""
题目描述

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
思路：

入队：将元素进栈A

出队：判断栈B是否为空，如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈；

如果不为空，栈B直接出栈。
"""


class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackB == []:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
        return self.stackB.pop()


"""
两个栈实现一个队列

入队：元素进栈A

出队：先判断栈B是否为空，为空则将栈A中的元素 pop 出来并 push 进栈B，再栈B出栈，如不为空则栈B直接出栈

复杂度分析：

这样用两个栈实现一个队列,入队的复杂度为O(1)，出队的复杂度则变为O(n)。

而直接用 python 的单个列表实现队列，以列表首作为队列尾，则入队用insert，复杂度为O(n)，出队用pop，复杂度为O(1)。（列表首，即列表中下标为0的元素）

实现：就以列表作为栈的底层实现，只要保证后进先出的约束就是栈。这里只实现入队和出队两个操作。
"""


class Queue:
    def __init__(self):
        self.stockA=[]
        self.stockB=[]
    def push(self, node):
        self.stockA.append(node)
    def pop(self):
        if self.stockB == []:
            if self.stockA == []:
                return None
            else:
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()


if __name__=='__main__':
    times=5
    testList=list(range(times))
    testQueue=Queue()
    for i in range(times):
        testQueue.push(testList[i])
    print(testList)
    for i in range(times):
        print(testQueue.pop(),',')   # end=''可以让 print 输出不换行
# 输出结果：先进先出
# [0, 1, 2, 3, 4]
# 0 ,1 ,2 ,3 ,4 ,