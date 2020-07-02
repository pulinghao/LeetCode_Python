#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/30 7:34 下午
@Author:  pulinghao
@File: 451. 根据字符出现频率排序.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def heapfy(self,arr,i):
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i
        if left < length and arr[largest][1] < arr[left][1]:
            largest = left

        if right < length and arr[largest][1] < arr[right][1]:
            largest = right

        if largest != i:
            arr[largest],arr[i] = arr[i],arr[largest]
            self.heapfy(arr,largest)

        pass

    def buildHeap(self,arr):
        for i in range(len(arr) // 2, -1, -1):
            self.heapfy(arr,i)

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1

        charList = []
        for k,v in map.items():
            charList.append([k,v])

        global length
        length = len(charList)
        self.buildHeap(charList)
        resStr = []
        res = ''
        for i in range(len(charList) - 1, -1 , -1):
            top = charList[0]
            res += str(top[0]) * int(top[1])
            charList[0],charList[i] = charList[i],charList[0]
            length -= 1
            self.heapfy(charList,0)
        return res

if __name__ == '__main__':
    out = Solution().frequencySort(s = "Aabb")

    print out 