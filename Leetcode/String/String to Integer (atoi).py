# -*- coding: utf-8 -*-


"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


# class Solution(object):
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         new_str = str.lstrip()
#         if new_str == '':
#             return 0
#         if not (new_str[0].isdigit() or new_str[0] == '-' or new_str[0] == '+'):
#             return 0
#         str_to_solve = ''
#         if new_str[0].isdigit():
#             for i in new_str:
#                 if i.isdigit():
#                     str_to_solve += i
#                 else:
#                     break
#         elif new_str == '-' or new_str == '+':
#             return 0
#         elif (new_str[0] == '-' or new_str[0] == '+' ) and new_str[1].isdigit() and len(new_str) > 1:
#             for i in range(1,len(new_str)):
#                 if new_str[i].isdigit():
#                     str_to_solve += new_str[i]
#                 else:
#                     break
#             str_to_solve = str_to_solve.lstrip('0')
#             if new_str[0] == '-':
#                 str_to_solve = int(str_to_solve) * -1
#             else:
#                 str_to_solve = int(str_to_solve)
#
#         else:
#             return 0
#
#         if int(str_to_solve) > pow(2, 31) or int(str_to_solve) < pow(-2, 31):
#             return pow(2, 31) * cmp(str_to_solve, 0)
#         return int(str_to_solve)


# class Solution(object):
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         temp = ''
#         temp1 = ''
#         new_str = ''
#         str = str.lstrip()
#         for i in str:
#             if not i.isalpha() and not i == ' ':
#                 temp += i
#             else:
#                 break
#         for i in temp:
#             if not i =='.':
#                 temp1 += i
#             else:
#                 break
#         for i in range(1,len(temp1)):
#             if not i == '-' or not i == '+':
#                 new_str += temp1[i]
#             else:
#                 break
#
#         new_str = new_str.rstrip()
#         if new_str.isdigit() and len(new_str) == 1:
#             return int(new_str)
#         if new_str == '' or (not new_str.isdigit() and len(new_str) == 1):
#             return 0
#         if new_str[0] == '.' or ((new_str[0] == '+' or new_str[0] == '-') and new_str[1] == '.'):
#             return 0
#         if not new_str[1:].isdigit():
#             return 0
#         if int(new_str) >= pow(2, 31):
#             return pow(2, 31) - 1
#         if int(new_str) <= pow(-2, 31):
#             return pow(-2, 31)
#         if new_str.isdigit():
#             return int(new_str)
#         else:
#             return int(new_str)


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0

        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >= '0' and c <= '9':
                # number = 10*number + ord(c) - ord('0')
                number = 10 * number + int(c)
            else:
                break
        number = flag * number
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number






x = " "
s = Solution()
print s.myAtoi(x)


# print cmp(x, 0)
# print pow(2, 31) * cmp(x, 0)

#
# s = ' '
# if s ==" ":
#     print 111
# else:
#     print 222

