#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/23 11:43 下午
 @Author  :pulinghao@baidu.com
 @File     :341. 扁平化嵌套列表迭代器.py
 @Description :
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       pass

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
        pass
   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       pass


class NestedIterator(object):

    def dfs(self, nests):
        for nest in nests:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self.dfs(nest.getList())

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        import collections
        self.queue = collections.deque()
        self.dfs(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.queue) else False