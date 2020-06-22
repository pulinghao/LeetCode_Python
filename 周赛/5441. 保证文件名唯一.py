#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/21 10:43 上午
 @Author   :pulinghao@baidu.com
 @File     :5441. 保证文件名唯一.py 
 @Description : 哈希
"""

import re
from collections import defaultdict


class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        fileDict = defaultdict(str)
        fileBackDict = defaultdict(str)  # 有后缀的
        ans = []

        for name in names:
            fileNum = re.findall(r'[(](.*?)[)]', name)
            if len(fileNum) == 0:
                # 没有后缀
                filename = name
                if fileDict[name] == "":
                    fileDict[name] = "0"
                    ans.append(filename)
                else:
                    fileback = int(fileDict[name])
                    fileback += 1
                    fileDict[name] = str(fileback)
                    fileBack = filename + '(' + str(fileback) + ')'
                    ans.append(fileBack)
                    if fileBackDict[fileBack] == "":
                        fileBackDict[fileBack] = '0'
            else:
                # 有后缀
                idx = name.find('(')
                back = fileNum[0]
                filenameNoTail = name[:idx]
                fileDict[filenameNoTail] = str(back)
                if fileBackDict[name] == "":
                    fileBackDict[name] = '0'
                    ans.append(name)
                else:
                    fileNum = int(fileBackDict[name])
                    fileNum += 1
                    fileBackDict[name] = str(fileNum)
                    ans.append(name + '(' + str(fileNum) + ')')

        return ans

    def answer2(self,names):
        dic = {}
        r = []
        n = len(names)
        for i in range(n):
            if names[i] not in dic:
                r.append(names[i])
                dic[names[i]] = 1
            else:
                j = dic[names[i]]
                while True:
                    newName = names[i] + "(" + str(j) + ")"
                    if newName not in dic:
                        dic[newName] = 1
                        r.append(newName)
                        break
                    dic[names[i]] = j + 1
                    j += 1
        return r

if __name__ == '__main__':
    print Solution().answer2(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"])