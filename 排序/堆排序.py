#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/30 3:34 下午
@Author:  pulinghao
@File: 堆排序.py
@Software: PyCharm

想象一下，给的数组就已经是一个二叉堆了，完全二叉树
本质是依次比较子树，从子树开始构建堆
"""

import leetcode_utils

class Heap(object):
    def buildMapHeap(self,arr):
        import math
        for i in range(len(arr) // 2, -1, -1):
            self.heapify(arr,i)


    def heapify(self,arr,i):
        #左子节点
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i # 最大数的索引，也即是根节点
        if left < arrLen and arr[left] > arr[largest]:
            largest = left
        if right < arrLen and arr[right] > arr[largest]:
            largest = right

        if largest != i: # 根节点不是最大
            self.swap(arr,i,largest)
            # 继续建堆，直到子树也满足 根节点大于叶子节点为止
            self.heapify(arr,largest)

    def swap(self,arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapSort(self,arr):
        global arrLen
        arrLen = len(arr)
        # 构建堆，这个时候第一个元素就是最大元素
        self.buildMapHeap(arr)
        for i in range(len(arr) - 1, 0 , -1):
            # 把堆头的元素放到队尾
            self.swap(arr,0,i)
            # 堆尾的元素不用参与排序，长度减1
            arrLen -= 1
            # 因为破坏了堆的结构，从堆顶开始重建堆
            # 最大的元素集中在堆顶的位置
            self.heapify(arr,0)
        return arr


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


if __name__ == '__main__':
    out = Heap().heapSort([8,1,2,6,3,4,10,5,11])

    print out 