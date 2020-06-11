#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/9 11:07 下午
 @Author   :pulinghao@baidu.com
 @File     :406. 根据身高重建队列.py 
 @Description :
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # 按照身高降序，再插入对应的人数,因为后面会身高矮的人插到前面去，身高高的人，满足局部最优解。当k一样时，身高矮的肯定在身高
        # 高的前面
        people.sort(key = lambda x:(-x[0],x[1]))
        res = []
        for p in people:
            res.insert(p[1],p)
        return res


if __name__ == '__main__':
    print Solution().reconstructQueue(people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])