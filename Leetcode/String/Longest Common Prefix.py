# -*- coding: utf-8 -*-


"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs) == 1:
#             return strs[0]
#
#         for i in range(len(strs) - 1):
#             if not strs[i] == strs[i+1]:
#                 break
#             elif i ==len(strs) and strs[i] == strs[i+1]:
#                 return strs[0]
#
#
#
#         # find the shortest str
#         shortest_len = pow(2, 31)
#
#         for i in strs:
#             if len(i) == 0:
#                 return ""
#             else:
#                 if len(i) <= shortest_len:
#                     shortest_len = len(i)
#         print shortest_len
#
#         strs_count = len(strs)   # count of strs
#         prefix = 0
#
#         for i in range(strs_count-1):
#             for j in range(shortest_len-1):
#                 if strs[i][j] == strs[i+1][j]:
#                     continue
#                 else:
#                     prefix = j
#
#         if prefix == 0:
#             return strs[0]
#         else:
#             return strs[0][0:prefix]


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


class Solution2(object):
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        minstrslen = 9999
        index = 0
        for i in range(0, len(strs)):
            if len(strs[i]) < minstrslen:
                minstrslen = len(strs[i])
                index = i
        ShortestString = strs[index]

        list = [0 for i in range(len(ShortestString))]
        for i in range(0, len(ShortestString)):
            for j in range(0, len(strs)):
                if strs[j][i] == ShortestString[i]:
                    list[i] += 1
        Prefix = ''
        for i in range(0, len(ShortestString)):
            if list[i] == len(strs):
                Prefix += ShortestString[i]
            else:
                break
        return Prefix








a = ["flow","flower","fl111"]
# a = ["dog","racecar","car"]
# a = ['c']
# a = ['a', 'c', 'c']
# a = ['']
s = Solution2()
# print a[0][0:1]
print s.longestCommonPrefix(a)