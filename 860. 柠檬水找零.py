#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/12/10 3:25 下午
@Author:  pulinghao
@File: 860. 柠檬水找零.py
@Software: PyCharm
"""

import leetcode_utils
import collections

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        pocket = collections.defaultdict(int)
        for bill in bills:
            if bill == 5:
                pocket[5] += 1
            elif bill == 10:
                if pocket[5] > 0:
                    pocket[5] -= 1
                    pocket[10] += 1
                else:
                    return False
            else:
                if pocket[10] > 0 and pocket[5] > 0:
                    pocket[10] -= 1
                    pocket[5] -= 1
                    pocket[20] += 1
                elif pocket[5] > 3:
                    pocket[5] -= 3
                    pocket[20] += 1
                else:
                    return False

        return True

if __name__ == '__main__':
    bills = [5,5,10,10,20]
    out = Solution().lemonadeChange(bills)

    print out
