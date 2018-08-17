# -*- coding: utf-8 -*-


"""
Given two arrays, write a function to compute their intersection.
Example:

Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
Note:

* Each element in the result should appear as many times as it shows in both arrays.
* The result can be in any order.
Follow up:

* What if the given array is already sorted? How would you optimize your algorithm?
* What if nums1's size is small compared to nums2's size? Which algorithm is better?
* What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3=[]
        if len(nums2) < len(nums1):
            for x in nums2:
                if x in nums1:
                    nums1.remove(x)
                    nums3.append(x)
            #nums4 = list(set(nums3))
            return nums3
        else:
            for x in nums1:
                if x in nums2:
                    nums2.remove(x)
                    nums3.append(x)
            #nums4 = list(set(nums3))
            return nums3

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

s = Solution()
print s.intersect(array1, array2)