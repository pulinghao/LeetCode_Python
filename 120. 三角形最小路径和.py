#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/14 10:09 上午
@Author:  pulinghao
@File: 120. 三角形最小路径和.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        newTriangle = []
        if len(triangle) > 0:
            newTriangle.append(triangle[0])
        else:
            return 0
        for i in range(1, len(triangle)):
            line = triangle[i]
            sumline = newTriangle[i - 1]
            newLine = []
            for j in range(len(line)):
                if j == 0:
                    sum = sumline[0] + line[0]
                elif j == len(line) - 1:
                    sum = sumline[-1] + line[-1]
                else:
                    sum1 = sumline[j - 1] + line[j]
                    sum2 = sumline[j] + line[j]
                    sum = min(sum1,sum2)
                newLine.append(sum)
            newTriangle.append(newLine)

        last = newTriangle[-1]
        res = min(last)
        return res



if __name__ == '__main__':
    line = "[]"
    triange = [

]
    out = Solution().minimumTotal(triange)

    print out 