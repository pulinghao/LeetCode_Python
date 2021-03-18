#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/14 5:01 下午
 @Author  :pulinghao@baidu.com
 @File     :765. 情侣牵手.py
 @Description :
"""

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row)
        res = 0
        for i in range(0, N - 1, 2):
            if (row[i] % 2 == 0 and row[i + 1] == row[i] + 1) or (row[i] % 2 == 1 and row[i + 1] == row[i] - 1):
            #if row[i] == row[i + 1] ^ 1:
                continue


            for j in range(i + 1, N):
                if row[j] == row[i] ^ 1:
                    row[j],row[i + 1] = row[i + 1],row[j]
                    res += 1
        return res


if __name__ == '__main__':
    row = [2,0,5,4,3,1]
    print Solution().minSwapsCouples(row)
