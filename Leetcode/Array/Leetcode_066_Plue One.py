# -*- coding: utf-8 -*-


"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 数组转换成数字
        intNum=0
        for i in range(len(digits)):
            intNum=intNum*10+digits[i]
        intNum+=1
        # 数字转换成字符
        strNum=str(intNum)
        # 字符转换成数组
        res=[]
        for i in range(len(strNum)):
            res.append(int(strNum[i]))
        return res

array = [9, 9, 9, 9]
s = Solution()
print s.plusOne(array)

"""
设定进位，从数组最后一个数开始和进位相加，判断是向下一位进位，还是自身是否加1
最后需要判断最高位是否进位，若进位则在数组开头插入1
"""


class Solution2():
    def plusOne(self, digits):
        count = 1  # 进位
        for i in range(len(digits)-1, -1, -1):
            if digits[i]+count == 10:
                count = 1
                digits[i] = 0
            else:
                digits[i] += count
                count = 0
        if count == 1:
            digits.insert(0, 1)
        return digits

s2 = Solution2()
print s2.plusOne(array)
