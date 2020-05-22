#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/28 10:02 上午
@Author:  pulinghao
@File: 面试题56 - I. 数组中数字出现的次数.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for n in nums:
            res = res ^ n

        h = 1
        while (h&res) == 0:  # 从右往左，找出第一位a和b不同的数字，例如1和6，第一位，是右边第一位
            h <<= 1

        ret = [0,0]
        for n in nums:
            if n & h != 0: #这里不能写 n&h == 1,因为h的值可能不是1，是10,100等等
                # a与h如果某个位置上的数字相同，那么a与b肯定不同
                ret[0] = ret[0]^n
            else:
                ret[1] = ret[1]^n
        pass
        return ret



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().singleNumbers(nums=[1,2,5,2])

    print out 