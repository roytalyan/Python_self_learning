# -*- coding: utf-8 -*-


"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        temp = []
        for i in range(len(s)):
            if s[i].isalnum():
                temp.append(s[i].lower())
        temp_rever = temp[::-1]
        return temp == temp_rever

x = ''
s = Solution()
print s.isPalindrome(x)