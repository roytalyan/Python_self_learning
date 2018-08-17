# -*- coding: utf-8 -*-


"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""


string = "hello"

# **********************Time Limit Exceeded**********************
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = []
        for i in s:
            temp.append(i)
        temp.reverse()
        new_string = ''
        for i in temp:
            new_string += i
        temp.append(new_string)
        return temp.pop()

s = Solution()
print s.reverseString(string)
# **********************Time Limit Exceeded**********************

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
