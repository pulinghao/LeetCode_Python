#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/17 10:33 上午
 @Author   :pulinghao@baidu.com
 @File     :141. 环形链表.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 快慢指针
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return True



if __name__ == '__main__':
    line = "[3,2,0,-4]"
    head = leetcode_utils.stringToListNode(line)
    line = "1"
    pos = leetcode_utils.stringToInt(line)

    ret = Solution().hasCycle(head,pos)

    out = (ret)
    print out
