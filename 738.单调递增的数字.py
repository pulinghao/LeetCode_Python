#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/15 7:31 下午
 @Author  :pulinghao@baidu.com
 @File     :738. 单调递增的数字.py
 @Description :
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        strN = str(N)
        listN = list(strN)
        max = -1
        idx = -1
        for i in range(len(listN) - 1):
            if max < int(listN[i]):
                max = int(listN[i])
                idx = i

            if int(listN[i]) > int(listN[i + 1]):
                listN[idx] = str(int(listN[idx]) - 1)
                for j in range(idx + 1 , len(listN)):
                    listN[j] = '9'

        return int(''.join(listN))

if __name__ == '__main__':
    N = 232
    out = Solution().monotoneIncreasingDigits(N)
    print out