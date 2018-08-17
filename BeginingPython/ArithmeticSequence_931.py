# -*- coding: utf-8 -*-

def checkIndex(key):
    """
    所给的键是能接受的索引吗?
    为了能被接受,键应该是一个非负整数. 如果不是一个整数,引发typeError; 如果是负数, 会引发IndexError
    """
    if not isinstance(key,(int, long)):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithemeticSequence:
    def __init__(self, start = 1, step = 1):
        """
        初始化算数序列

        start: 第一个值
        step: 亮哥相邻值之间的差别
        改变: 用户修改的值的字典
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        Get an item from Arithemitic Sequence
        """
        checkIndex(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        """
        修改算数序列中的一个项
        """
        checkIndex(key)

        self.changed[key] = value

s = ArithemeticSequence(1,2)
print s[4]
s[5]=1
print s.changed