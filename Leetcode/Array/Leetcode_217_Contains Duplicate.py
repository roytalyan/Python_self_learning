# -*- coding: utf-8 -*-


"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false
if every element is distinct.
Example 1:
Input: [1,2,3,1]
Output: true
Example 2:
Input: [1,2,3,4]
Output: false
Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        temp = dict()
        for num in nums:
            if temp.has_key(num):
                temp[num] += 1
                if temp[num] >= 2:
                    return True
            else:
                temp[num] = 1
        return False

s = Solution()
array = [9, 1, 2, 1]
print s.containsDuplicate(array)


# *****************暴力会超时****************

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for x in range(0, len(nums)):
            j = nums.count(nums[x])
            if nums.count(nums[x]) != 1:
                return True
        return False

test = Solution()
print test.containsDuplicate([3, 1, 2])
# *****************暴力会超时****************

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for x in range(0, len(nums)-1):
            if nums[x] == nums[x+1]:
                return True
        return False