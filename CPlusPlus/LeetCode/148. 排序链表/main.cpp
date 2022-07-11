//
//  main.cpp
//  148. 排序链表
//
//  Created by pulinghao on 2022/6/29.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // 归并排序
        if(!head || !head->next){
            return head;
        }

        // 1. 找终点
        ListNode *slow = head;
        ListNode *fast = head;
        while(fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode *midHead = slow->next;

        // 断链
        slow->next = NULL;

        // 归并
//        ListNode *res = (ListNode *)malloc(sizeof(ListNode));
        ListNode *res = new ListNode(0);
        ListNode *p = res;
        res->val = 0;
        ListNode *left = sortList(head);
        ListNode *right = sortList(midHead);
        while(left && right){
            if(left->val < right->val){
                p->next = left;
                left = left->next;
            } else {
                p->next = right;
                right = right->next;
            }
            p = p->next;
        }

        if(left){
            p->next = left;
        } else{
            p->next = right;
        }
        return res->next;

    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
