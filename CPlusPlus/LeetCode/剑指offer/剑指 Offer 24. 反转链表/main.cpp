//
//  main.cpp
//  剑指 Offer 24. 反转链表
//
//  Created by pulinghao on 2022/6/12.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = NULL;
        ListNode* cur = head;
        while (cur) {
            // 获取下个节点
            ListNode *next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
    
    ListNode *recursiveReverseList(ListNode *head){
        if (!head || !head->next) {
            return head;
        }
        ListNode *node = recursiveReverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return node;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string list = "[1,2,3,4,5]";
    ListNode *head = stringToListNode(list);
    head = Solution().recursiveReverseList(head);
    string res = listNodeToString(head);
    std::cout << res<<endl;
    return 0;
}
