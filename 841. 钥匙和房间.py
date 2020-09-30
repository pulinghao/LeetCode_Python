#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/8/31 1:33 下午
@Author:  pulinghao
@File: 841. 钥匙和房间.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = []
        enters = [0] * len(rooms)
        firstRoom = rooms[0]
        for key in firstRoom:
            queue.append(key)

        enters[0] = 1
        while queue:
            top = queue.pop(0)
            if enters[top] == 1:
                continue
            enters[top] = 1
            keys = rooms[top]
            for key in keys:
                queue.append(key)

        res = True
        for enter in enters:
            if enter == 0:
                res = False
                break

        return res


if __name__ == '__main__':
    rooms =[[]]
    out = Solution().canVisitAllRooms(rooms)

    print out
