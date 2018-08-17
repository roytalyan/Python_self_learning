# -*- coding: utf-8 -*-


"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

x = 'loveleetcode'
# print len(s)
# print s[1]
# for x in range(len(x)):
#     print x


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = dict()
        for x in range(len(s)):
            if not temp.has_key(s[x]):
                temp[s[x]] = 1
            else:
                temp[s[x]] += 1
        for y in range(len(s)):
            if temp[s[y]] == 1:
                return y
            else:
                continue
        return -1

s = Solution()
print s.firstUniqChar(x)

