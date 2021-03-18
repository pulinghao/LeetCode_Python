#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/6 10:59 下午
 @Author  :pulinghao@baidu.com
 @File     :1423. 可获得的最大点数.py
 @Description :
"""


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        N = len(cardPoints)
        res = 0

        A = [0] * (len(cardPoints) + 1)
        B = [0] * (len(cardPoints) + 1)
        A[0] = 0
        B[0] = 0
        for i in range(N):
            # i = 0表示右侧一张都不拿
            A[i + 1] = A[i] + cardPoints[i]
            B[i + 1] = B[i] + cardPoints[-i - 1]

        for i in range(k + 1):
            res = max(A[i] + B[k - i], res)
        return res


if __name__ == '__main__':
    cardPoints = [96,90,41,82,39,74,64,50,30]
    k = 8
    print Solution().maxScore(cardPoints, k)
