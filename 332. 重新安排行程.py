#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/27 12:16 上午
 @Author  :pulinghao@baidu.com
 @File     :332. 重新安排行程.py
 @Description :
"""
import heapq
import collections
class Solution(object):
    def __init__(self):
        self.res = []
        self.ans = []
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(cur):
            while vec[cur]:
                tmp = heapq.heappop(vec[cur])
                dfs(tmp)
            stack.append(cur)

        vec = collections.defaultdict(list)
        for depart,arrive in tickets:
            vec[depart].append(arrive)

        stack = list()
        dfs('JFK')
        return stack[::-1]

    def dfs(self,path,cur,idx,N,dic):
        if idx == N:
            self.ans.append(path[:])
            return True

        if idx < N:
            if cur not in dic:
                return False

            values = dic[cur]
            newvalues = values[:]
            for key in newvalues:
                path.append(key)
                values.remove(key)
                self.dfs(path,key,idx + 1, N,dic)
                path.remove(key)
                values.append(key)

    def bfs(self,path,nodes):
        queue = ['JFK']
        last = ''
        while queue:
            top = queue.pop(0)
            path.append(top)
            if top in nodes.keys():
                if last in nodes.keys():
                    lastNode = nodes[last]
                    lastNode.remove(top)
                sons = nodes[top]
                for son in sons:
                    queue.append(son)
                    last = top
            else:
                lastNode = nodes[last]
                lastNode.remove(top)
                if not self.clear(nodes):
                    path.pop(-1)
                    lastNode.append(top)


    def clear(self,dict):
        res = True
        for key in dict.keys():
            value = dict[key]
            if len(value) != 0:
                res = False
                return res
        return res



        pass

if __name__ == '__main__':
    # tickets1 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    tickets1 = [["JFK","AAA"],["JFK","BBB"],["BBB","JFK"]]

    tickets =  [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print Solution().findItinerary(tickets1)