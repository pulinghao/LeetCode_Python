#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/10 10:33 下午
 @Author   :pulinghao@baidu.com
 @File     :24. 两两交换链表中的节点.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.swap(head)
        pass
    def swap(self, node):
        # 1.确定终止条件
        if not node or not node.next:
            return node

        # 2.中间态
        newHead = self.swap(node.next.next)

        # 把node.next暂存起来
        nextNode = node.next

        # 移动指针
        node.next = newHead
        nextNode.next = node

        # 返回值是当前节点的下一个节点
        return nextNode



if __name__ == '__main__':
    list = "[1,2,3,4]"
    head1 = leetcode_utils.stringToListNode(list)

    result = Solution().swapPairs(head1)

    resultString = leetcode_utils.listNodeToString(result)
    print resultString