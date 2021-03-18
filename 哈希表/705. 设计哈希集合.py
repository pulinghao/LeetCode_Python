#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/13 12:15 上午
 @Author  :pulinghao@baidu.com
 @File     :705. 设计哈希集合.py
 @Description :
"""

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = [-1] * 10 ** 5
        self.hashKey = 10 ** 5

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashTable[key % self.hashKey] = key


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashTable[key % self.hashKey] = -1


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return True if self.hashTable[key % self.hashKey] != -1 else False