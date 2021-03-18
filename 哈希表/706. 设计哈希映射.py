#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/14 11:05 下午
 @Author  :pulinghao@baidu.com
 @File     :706. 设计哈希映射.py
 @Description :
"""

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashCode = 10 ** 6
        self.hashMap = [-1] * self.hashCode


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashMap[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.hashMap[key]


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.hashMap[key] = -1

