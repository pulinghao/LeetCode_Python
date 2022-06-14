#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/6/13 12:57
@Author:  pulinghao
@File: 1051. 高度检查器.py
@Software: PyCharm
"""

import leetcode_utils


class Solution ( object ) :
    def __init__ ( self ) :
        pass

    def func ( self , root ) :
        pass

    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        m = max(heights)
        cnt = [0] * (m + 1)

        for h in heights:
            cnt[h] += 1

        idx = ans = 0
        for i in range(1, m + 1):
            for j in range(cnt[i]):
                if heights[idx] != i:
                    ans += 1
                idx += 1

        return ans



if __name__ == '__main__' :
    line = "[]"
    root = leetcode_utils.stringToTreeNode ( line )

    out = Solution ( ).func ( root )

    print out
