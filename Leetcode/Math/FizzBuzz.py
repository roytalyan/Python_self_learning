# -*- coding: utf-8 -*-

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = list(range(1, n+1))
        newarr = []
        for n in arr:
            if n % 3 == 0 and n % 5 == 0:
                newarr.append('FizzBuzz')
            elif n % 3 == 0 and n % 5 != 0:
                newarr.append('Fizz')
            elif n % 5 == 0 and n % 3 != 0:
                newarr.append('Buzz')
            else:
                newarr.append(str(n))
        return newarr