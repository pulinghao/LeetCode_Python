#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/28 9:40 上午
 @Author  :pulinghao@baidu.com
 @File     :657. 机器人能否返回原点.py
 @Description :
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dirs = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
        loc = [0,0]
        for move in moves:
            dir = dirs[move]
            x = loc[0] + dir[0]
            y = loc[1] + dir[1]
            loc = [x,y]

        if loc[0] == 0 and loc[1] == 0:
            return True
        else:
            return False




if __name__ == '__main__':
    moves = "LL"
    print Solution().judgeCircle(moves)
