#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/5 3:14 下午
 @Author   :pulinghao@baidu.com
 @File     :234. 回文链表.py 
 @Description :
"""

import leetcode_utils

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        # 1. 先找到链表中间节点
        fast = head  # 一次走两步
        slow = head  # 一次走一步
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next


        # 2. 从slow的位置反转前半段链表
        if not fast.next:
            # 奇数个
            cur = head
            pre = None
            while cur != slow:
                next = cur.next  #保存next指针
                cur.next = pre   #将当前的指针指向前驱
                pre = cur        #将前驱移到当前
                cur = next       #将当前挪到下一个

            reveseHead = ListNode(slow.val)
            reveseHead.next = pre

            other = reveseHead
            while slow:
                if slow.val == other.val:
                    slow = slow.next
                    other = other.next
                else:
                    return False
            return True
        if not fast.next.next:
            # 2.偶数个
            cur = head
            pre = None
            slow_next = slow.next # 把这个点保存一下
            while cur != slow_next:
                next = cur.next  # 保存next指针
                cur.next = pre  # 将当前的指针指向前驱
                pre = cur  # 将前驱移到当前
                cur = next  # 将当前挪到下一个

            reversHead = pre
            slow = slow_next
            other = reversHead
            while slow:
                if slow.val == other.val:
                    slow = slow.next
                    other = other.next
                else:
                    return False
            return True
            pass

if __name__ == '__main__':
    list = "[]"
    head1 = leetcode_utils.stringToListNode(list)

    result = Solution().isPalindrome(head1)
    print result