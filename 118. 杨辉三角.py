#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/6 9:43 下午
 @Author  :pulinghao@baidu.com
 @File     :118. 杨辉三角.py
 @Description :
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []
        res = []
        temp = []
        for i in range(1,numRows + 1):
            if i == 1:
                temp = [1]
                res.append(temp)
                continue

            if i == 2:
                temp = [1,1]
                res.append(temp)
                continue

            last = temp
            temp = []
            for j in range(i):
                if j == 0:
                    temp.append(last[j])
                    continue
                if j == i - 1:
                    temp.append(last[j - 1])
                    continue

                temp.append(last[j - 1] + last[j])
            res.append(temp)

        return res

if __name__ == '__main__':
    out = Solution().generate(numRows=0)
    print out