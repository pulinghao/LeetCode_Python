#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/2 10:17 下午
 @Author  :pulinghao@baidu.com
 @File     :239. 滑动窗口最大值.py
 @Description :
"""
import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans



if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print Solution().maxSlidingWindow(nums,k)

