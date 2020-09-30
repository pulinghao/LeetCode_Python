#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/27 11:08 上午
@Author:  pulinghao
@File: 5525. 皇位继承顺序.py
@Software: PyCharm
"""

import leetcode_utils
import collections
class TreeNode(object):
    def __init__(self,name):
        self.name = name
        self.chidren = []
        self.status = False

class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.dict = {}
        self.liveDict = {}
        self.dict[kingName] = []
        self.liveDict[kingName] = True
        self.orderList = [kingName]
        self.kingName = kingName


    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.dict[parentName].append(childName)
        self.dict[childName] = []
        self.liveDict[childName] = True


    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.liveDict[name] = False


    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        def pre_order(x):
            cur_order = [x]
            for nxt in self.dict[x]:
                cur_order += pre_order(nxt)
            return cur_order
        order = pre_order(self.kingName)
        return [p for p in order if self.liveDict[p]]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


if __name__ == '__main__':
    t = ThroneInheritance('king')
    t.birth("king", "cycle")#// 继承顺序：king > andy
    t.birth("cycle", "shannon")#// 继承顺序：king > andy > bob
    t.birth("shannon", "scoot")# // 继承顺序：king > andy > bob > catherine
    t.birth("king", "keith")# // 继承顺序：king > andy > matthew > bob > catherine
    t.birth("cycle", "jos")# // 继承顺序：king > andy > matthew > bob > alex > catherine
    # t.birth("bob", "asha")# // 继承顺序：king > andy > matthew > bob > alex > asha > catherine
    print t.getInheritanceOrder()# // 返回["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
    # t.death("bob")# // 继承顺序：king > andy > matthew > bob（已经去世） > alex > asha > catherine
    # print t.getInheritanceOrder()# // 返回["king", "andy", "matthew", "alex", "asha", "catherine"]
