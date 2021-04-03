#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/19 10:49 下午
 @Author  :pulinghao@baidu.com
 @File     :1603. 设计停车系统.py
 @Description :
"""


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.parks = [0,0,0,0]
        self.parks[1] = big
        self.parks[2] = medium
        self.parks[3] = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        rest = self.parks[carType]
        if rest > 0:
            self.parks[carType] = self.parks[carType] - 1
            return True
        else:
            return False
