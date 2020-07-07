#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/30 11:38 下午
 @Author   :pulinghao@baidu.com
 @File     :1226. 哲学家进餐.py 
 @Description :
"""

import threading


class DiningPhilosophers(object):
    def __init__(self):
        self.lock = threading.Lock()

        # func2
        self.cv = threading.Condition()
        self.d = {}
        for i in range(5):
            self.d[i] = False

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        """
        :type philosopher: int
        :type pickLeftFork: method
        :type pickRightFork: method
        :type eat: method
        :type putLeftFork: method
        :type putRightFork: method
        :rtype: void
        """
        self.wantsToEatFunc1(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)

    def wantsToEatFunc1(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        """ 使用线程解决
        :param philosopher:
        :param pickLeftFork:
        :param pickRightFork:
        :param eat:
        :param putLeftFork:
        :param putRightFork:
        :return:
        """
        self.lock.acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()
        self.lock.release()

    def wantsToEatFunc2(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        """

        :param philosopher:
        :param pickLeftFork:
        :param pickRightFork:
        :param eat:
        :param putLeftFork:
        :param putRightFork:
        :return:
        """
        left = philosopher - 1
        right = philosopher + 1

        if left < 0:
            left = 4
        if right > 4:
            right = 1

        with self.cv:
            self.cv.wait_for(lambda: not self.d[left] and not self.d[right])
            self.d[philosopher] = True
            pickLeftFork()
            pickRightFork()
            eat()
            putRightFork()
            putLeftFork()

        self.d[philosopher] = False
