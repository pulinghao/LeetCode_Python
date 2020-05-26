#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/25 10:50 上午
@Author:  pulinghao
@File: 146. LRU缓存机制.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = []


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for pair in self.cache:
            if pair[0] == key:
                item = pair
                index = self.cache.index(pair)
                self.cache.pop(index)
                self.cache.append(item)
                return item[1]

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 1. 如果有空间
        for pair in self.cache:
            if pair[0] == key:
                item = pair
                index = self.cache.index(pair)
                self.cache.pop(index)
                item[1] = value
                self.cache.append(item)
                return

        if len(self.cache) + 1 > self.capacity:
            self.cache.pop(0)
        self.cache.append([key,value])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","put","get"]
# [[2],        [2,1],[2,2],[2],[1,1],[4,1],[2]]


# 双向链表法:
class DLinkNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.cache = dict()
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def addToHead(self,node):
        # 这里不是把新节点作为head，而是把head.next作为第一个节点
        # 保存head的下一个节点
        last = self.head.next
        self.head.next = node
        node.prev = self.head
        last.prev = node
        node.next = last

    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self,node):
        # 先把节点移除，再放到头部
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def get(self,key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            node = DLinkNode(key,value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                remove = self.removeTail()
                self.cache.pop(remove.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    print cache.get(2)
    cache.put(1, 1)
    # print cache.get(2)
    cache.put(4, 1)
    print cache.get(2)
    # print cache.get(3)
    # print cache.get(4)
