#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/29 4:15 下午
@Author:  pulinghao
@File: 347. 前 K 个高频元素.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def simpleHeap(self,arr,i):
        left = 2 * i + 1
        right = 2 * i + 2

        minIdx = i
        if left < arrLen and arr[minIdx][1] < arr[left][1]:
            minIdx = left

        if right < arrLen and arr[minIdx][1] < arr[right][1]:
            minIdx = right

        if minIdx != i:
            arr[minIdx],arr[i] = arr[i], arr[minIdx]
            self.simpleHeap(arr,minIdx)

    def buildHeap(self,arr,size):
        for i in range(len(arr) / 2,-1,-1):
            self.simpleHeap(arr,i)
        pass

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1.维护一个最大堆
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        # 2.构建最大堆
        hashlist = []
        for key,value in map.items():
            hashlist.append([key,value])

        global arrLen
        arrLen = len(hashlist)
        res = []
        self.buildHeap(hashlist,arrLen)
        for i in range(len(hashlist) - 1, len(hashlist) - k - 1, -1):
            res.append(hashlist[0][0])
            hashlist[0],hashlist[i] = hashlist[i],hashlist[0]
            arrLen -= 1
            self.simpleHeap(hashlist,0)
        return res

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)

    print out 