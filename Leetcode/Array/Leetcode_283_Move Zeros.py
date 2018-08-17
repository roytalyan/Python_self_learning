# -*- coding: utf-8 -*-


"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
Note:

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0  # 0的个数
        for x in range(0, len(nums)-zero):
            while nums[x] == 0 & x < len(nums)-zero:
                zero += 1
                del nums[x]
                nums.append(0)
        return nums


array = [0, 2, 3, 8, 0, 0, 0, 9]
s = Solution()
print s.moveZeroes(array)