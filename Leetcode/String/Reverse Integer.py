# -*- coding: utf-8 -*-


"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

x = 153423646


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return int(str(x)[::-1])
        x = -x
        return -int(str(x)[::-1])


class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = int(str(abs(x))[::-1])  # abs()取绝对值
        if y > pow(2, 31):  # pow(x, y) : x的y次方
            return 0
        return y * cmp(x, 0)  # cmp() if x > 0 : 1 ; if x < 0 : -1

s = Solution1()
print s.reverse(x)
