# -*- coding: utf-8 -*-


"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        list = range(1, n)[2::2]
        result = [2]
        for i in list:
            for j in range(2, i):
                tag = False
                if i % j == 0:
                    tag = True
                    break
            if not tag:
                result.append(i)
        return result

s = Solution()
x = s.countPrimes(100)
print x
print len(x)