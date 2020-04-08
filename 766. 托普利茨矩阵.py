#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/3 10:42 上午
@Author:  pulinghao
@File: 766. 托普利茨矩阵.py
@Software: PyCharm
"""

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        rows = len(matrix)
        first_line = matrix[0]
        cols = len(first_line)

       # 从左下角开始，先往上，再往右进行遍历
        for i in range(rows - 1):
            x = rows - 1 - i
            y = 0
            head = matrix[x][y]

            a = x
            b = y
            while a < rows and b < cols:
                if head != matrix[a][b]:
                    return False
                a += 1
                b += 1

        for j in range(cols):
            x = 0
            y = j
            head = matrix[x][y]
            a = x
            b = y
            while a < rows and b < cols:
                if head != matrix[a][b]:
                    return False
                a += 1
                b += 1

        return True
        pass


        # 另一种做法是把前一行的最后一个元素去掉，然后和下一行去掉第一个元素去掉，两行是否相等即可
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 1 or cols == 1:
            return True

        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False

        return True


if __name__ == '__main__':
    matrix = [
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]
    ]
    # matrix = [
    #     [1, 2],
    #     [2, 2]
    # ]
    print Solution().isToeplitzMatrix(matrix)