#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/25 6:56 下午
@Author:  pulinghao
@File: 744. 寻找比目标字母大的最小字母.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1

        if ord(target) < ord(letters[0]):
            return letters[0]

        if ord(target) >= ord(letters[-1]):
            return letters[0]

        while left < right:
            mid = left + (right - left) // 2
            if ord(letters[mid]) < ord(target): # 这里之所以取等号，是因为相等的时候，要取右边的值
                left = mid + 1
            elif ord(letters[mid]) == ord(target):
                left = mid + 1
            else:
                right = mid

        return letters[left]




if __name__ == '__main__':
    out = Solution().nextGreatestLetter(letters=["e","e","e","e","e","e","n","n","n","n"],target="e")

    print out 