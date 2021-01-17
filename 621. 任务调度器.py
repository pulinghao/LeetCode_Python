#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/5 10:13 下午
 @Author  :pulinghao@baidu.com
 @File     :621. 任务调度器.py
 @Description :
"""

import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskDict = collections.defaultdict(int)
        for task in tasks:
            taskDict[task] += 1
