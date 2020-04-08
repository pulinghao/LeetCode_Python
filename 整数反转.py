#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/31 12:26 下午
@Author:  pulinghao
@File: 整数反转.py
@Software: PyCharm
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # array = []
        # simbol = 0  #符号位
        # result = 0
        # if x <= 0:
        #     simbol = 1
        #     x = -x
        # while x / 10 != 0:
        #     rest = x % 10
        #     x = x/10
        #     array.append(rest)
        # array.append(x)
        #
        # for num in array:
        #     result = num + result * 10
        #
        # if simbol == 1:
        #     result = -result
        #
        # if result > 2147483647 or result < -2147483648:
        #     return 0
        # return result
        if x == 0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x) - 1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        return 0


if __name__ == '__main__':
    solve = Solution()


    print solve.reverse(123)
