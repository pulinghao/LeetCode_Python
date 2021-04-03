#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/31 8:50 下午
 @Author  :pulinghao@baidu.com
 @File     :字节.py
 @Description :
"""
def func(array):
    left = 0
    right = 1
    maxLength = 0
    maxLeft = -1
    maxRight = -1

    while right < len(array):
        if array[right] < array[right - 1]:
            right += 1
        else:
            length = right - left - 1
            if length > maxLength:
                maxLeft = left
                maxRight = right
            left = right
            right += 1
    return array[maxLeft:maxRight]


array = [1,2,3,4,6,5,3,-1,4,0]
print func(array)