#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/2 6:45 下午
@Author:  pulinghao
@File: 485. 最大连续1的个数.py
@Software: PyCharm
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
"""



class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        temp = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                temp += 1
                if temp > res:
                    res = temp
            else:
                temp = 0
            i += 1
        return res





if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    print  Solution().findMaxConsecutiveOnes(nums)

    ''.join(map(str, nums)).split('0') # 将nums数组转成字符串后，用0进行分割

    print ''.join(map(str,nums)).split('0')
    # print max(map(len, ''.join(map(str, nums)).split('0')))