#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/21 8:23 下午
@Author:  pulinghao
@File: 345. 反转字符串中的元音字母.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isMetaChar(s):
            if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'\
                    or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U':
                return True
            else:
                return False
        left = 0
        right = len(s) - 1

        s1 = list(s)
        while left < right:
            while not isMetaChar(s1[left]) and left < right:
                left += 1

            while not isMetaChar(s1[right]) and right > left:
                right -= 1
            if left < right:
                temp = s1[left]
                s1[left] = s1[right]
                s1[right] = temp

                left += 1
                right -=1

        return ''.join(s1)



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().reverseVowels(s=".,")

    print out 