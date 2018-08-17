# -*- coding: utf-8 -*-


"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
* Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
* Could you do it in-place with O(1) extra space?
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 1:
            new_num = nums[-1]
            del nums[-1]
            nums.reverse()
            nums.append(new_num)
            nums.reverse()
        else:
            for x in range(-k-1, -1):
                new_num = nums[-1]
                del nums[-1]
                nums.reverse()
                nums.append(new_num)
                nums.reverse()
        return nums

test = Solution()
print test.rotate([1, 2, 3, 4, 5, 6, 7], 4)

# k = k % len(nums)
# nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]