# -*- coding: utf-8 -*-


"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):  # 超时
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):  # len不同直接False
            temp_t = dict()
            for i in range(len(t)):
                if not temp_t.has_key(t[i]):
                    temp_t[t[i]] = 1
                else:
                    temp_t[t[i]] += 1  # 把T构建字典, 里面的字母做key value = 出现次数
            for j in range(len(s)):
                count = s.count(s[j])   # 统计字母在s出现的次数
                if not (temp_t.has_key(s[j]) and temp_t[s[j]] == count):
                    return False
            return True
        return False


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        temp_s = {}
        temp_t = {}

        for c in s:
            temp_s[c] = temp_s.get(c, 0) + 1

        for c in t:
            temp_t[c] = temp_t.get(c, 0) + 1

        return temp_s == temp_t

x = 'aacc'
y = 'ccac'

s = Solution3()
print s.isAnagram(x, y)