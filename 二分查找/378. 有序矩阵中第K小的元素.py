#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/2 10:38 上午
@Author:  pulinghao
@File: 378. 有序矩阵中第K小的元素.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def check(num):
            """

            :param num: 检查这个数字是否满足题意
            :return:
            """
            i = len(matrix) - 1
            j = 0
            idx = 0
            while i >= 0 and j < len(matrix):
                if matrix[i][j] <=num:
                    idx += i + 1
                    # 往右边找,右边的数字肯定比左边的大
                    j += 1
                else:
                    # 往上边找，上边的数字肯定比左边的小
                    i -= 1

            return idx

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left <= right:
            mid = left + (right - left) / 2
            #
            idx = check(mid)
            # 寻找左边界
            if idx == k:
                # 找到答案的时候，向左侧收缩
                right = mid - 1
            elif idx > k:
                right = mid - 1
            else:
                left = mid + 1

        return left




if __name__ == '__main__':
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 8
    out = Solution().kthSmallest(matrix,k)

    print out 