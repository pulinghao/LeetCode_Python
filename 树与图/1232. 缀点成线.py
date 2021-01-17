#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/17 11:30 下午
 @Author  :pulinghao@baidu.com
 @File     :1232. 缀点成线.py
 @Description :
"""

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True

        res = True
        for i in range(1, len(coordinates) - 1):
            a = coordinates[i - 1]
            b = coordinates[i]
            c = coordinates[i + 1]

            aby = b[1] - a[1]
            abx = b[0] - a[0]

            bcy = c[1] - b[1]
            bcx = c[0] - b[0]

            if abx == 0 and bcx == 0:
                continue
            elif abx == 0 and bcx != 0:
                res = False
                break
            elif abx != 0 and bcx == 0:
                res = False
                break
            else:
                kab = aby * 1.0 / abx
                kbc = bcy * 1.0 / bcx
                if kab == kbc:
                    continue
                else:
                    res = False
                    break

        return res

if __name__ == '__main__':
    coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    print Solution().checkStraightLine(coordinates)
