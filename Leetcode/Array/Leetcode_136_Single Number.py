# -*- coding: utf-8 -*-


"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        B = {}
        for i in A:
            if i not in B:
                B[i] = 1
            else:
                B[i] = 2
        for i in B:
            if B[i] == 1:
                ret = i
                break
        return ret

s = Solution()

array = [1, 2, 3, 3, 2]
print s.singleNumber(array)