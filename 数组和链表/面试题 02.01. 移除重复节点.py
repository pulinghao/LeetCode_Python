#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/26 10:33 上午
 @Author   :pulinghao@baidu.com
 @File     :面试题 02.01. 移除重复节点.py 
 @Description :
"""
import leetcode_utils
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        cur = head
        pre = None
        while cur:
            if cur.val in dic:
                pre.next = cur.next
            else:
                dic[cur.val] = 1
                pre = cur
            cur = cur.next

        return head


if __name__ == '__main__':
    line = "[1]"
    head = leetcode_utils.stringToListNode(line)

    ret = Solution().removeDuplicateNodes(head)

    out = leetcode_utils.listNodeToString(ret)
    print out