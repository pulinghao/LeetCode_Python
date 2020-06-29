#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/28 11:01 上午
 @Author   :pulinghao@baidu.com
 @File     :5448. 判断路径是否相交.py 
 @Description :
"""

class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        cur = [0,0]
        paths = [cur]
        for step in path:
            if step == 'N':
                next = [cur[0],cur[1] + 1]
                cur = next
                if next in paths:
                    return True
                paths.append(next)
            if step == 'S':
                next = [cur[0],cur[1] - 1]
                cur = next
                if next in paths:
                    return True
                paths.append(next)
            if step == 'E':
                next = [cur[0] + 1,cur[1]]
                cur = next
                if next in paths:
                    return True
                paths.append(next)
            if step == 'W':
                next = [cur[0] - 1,cur[1]]
                cur = next
                if next in paths:
                    return True
                paths.append(next)
        return False


if __name__ == '__main__':
    print Solution().isPathCrossing(path = "EESESSWSE")