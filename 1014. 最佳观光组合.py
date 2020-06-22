#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/17 4:04 下午
 @Author   :pulinghao@baidu.com
 @File     :1014. 最佳观光组合.py 
 @Description : 前缀和 + 数学
"""


class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 1.暴利
        # res = 0
        # for i in range(len(A)):
        #     for j in range(i + 1, len(A)):
        #         res = max(res,A[j] + A[i] + i - j)
        #
        # return res

        res = 0
        pre_max = A[0] + 0
        for i in range(1,len(A)):
            res = max(res,pre_max + A[i] - i)
            pre_max = max(pre_max, A[i] + i)
        return res

if __name__ == '__main__':
    print Solution().maxScoreSightseeingPair([6, 9, 10, 5, 9, 10, 4, 5])
