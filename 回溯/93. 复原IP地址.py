#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/9 10:11 下午
 @Author   :pulinghao@baidu.com
 @File     :93. 复原IP地址.py 
 @Description :
"""

class Solution(object):
    def __init__(self):
        self.res = []
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        path = [0,0,0,0]
        self.backtrace(s,0,0,path)
        return self.res

    def backtrace(self,s,start,segNum,path):
        # 终止条件
        if segNum == 4:
            if start == len(s):
                # 到达终点
                ans = ""
                for i in range(0,3):
                    ans += str(path[i]) + '.'
                ans += str(path[-1])
                self.res.append(ans)
            return

        if start == len(s):
            # 长度不够分成4段
            return

        if s[start] == '0':
            path[segNum] = s[start]
            self.backtrace(s,start + 1,segNum + 1,path)

        temp = 0
        for end in range(start, len(s)):
            temp = 10 * temp + int(s[end])
            if 0 < temp <= 255:
                # 这里不能等于0,因为0的情况被单独处理了
                path[segNum] = temp
                self.backtrace(s,end + 1,segNum + 1,path)
            else:
                break


if __name__ == '__main__':
    print Solution().restoreIpAddresses("25525511135")