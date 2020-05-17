#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/16 6:23 下午
 @Author   :pulinghao@baidu.com
 @File     :66. 加一.py 
 @Description :
"""
import copy

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        zero = True
        another = copy.deepcopy(digits)
        for i in range(len(another) - 1, -1 , -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                zero = False
                break

        if not zero:
            return digits
        else:
            newdigits = [0 for _ in range(len(digits) + 1)]
            newdigits[0] = 1
            return newdigits




if __name__ == '__main__':
    print Solution().plusOne(digits=[8,9,9,9])