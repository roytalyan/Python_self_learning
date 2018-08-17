# -*- coding: utf-8 -*-


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        for x in range(0, len(nums)):
            firstNum = nums[x]
            secondNum = target - firstNum
            if secondNum in nums:
                j = nums.index(secondNum)
                if x != j:
                    answer.append(x)
                    answer.append(j)
                    return answer

test = Solution()
print test.twoSum([3, 2, 1, 4],5)

"""
使用最基础的两重循环
"""


class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        result = []
        for i in range(0,length):
            for j in range(i,length):
                tSum = nums[i] + nums[j]
                if tSum == target and i != j:
                    result.append(i)
                    result.append(j)
                    return result


"""
使用一重循环，用target减去第一个值，判断第二个值是否在列表中（注意也要判断index是否相同）
"""


class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(0,len(nums)):
            oneNum = nums[i]
            twoNum  = target - oneNum
            if twoNum in nums:
                j = nums.index(twoNum)
                if i != j:
                    result.append(i)
                    result.append(j)
                    return result