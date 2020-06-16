#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/15 8:56 下午
 @Author   :pulinghao@baidu.com
 @File     :763. 划分字母区间.py 
 @Description :
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        # 存储键值,把每个元素的最后一次出现的位置保存下来
        dic = {item: idx for idx, item in enumerate(S)}
        start = 0
        end = 0
        ans = []
        for i, element in enumerate(S):
            # 第i个元素，最后一次出现的位置为dic[element]
            end = max(end,dic[element])
            if i == end: # 遍历的位置与end重合
                ans.append(end - start + 1)
                start = i + 1

        return ans

if __name__ == '__main__':
    print Solution().partitionLabels(S = "ababcbacadefegdehijhklij")
