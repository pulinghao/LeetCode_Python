//
//  main.cpp
//  剑指 Offer 18. 删除链表的节点
//
//  Created by pulinghao on 2022/6/1.
//

#include <iostream>
#include "common.h"
class Solution {
public:
    ListNode* deleteNode(ListNode* head, int val) {
//        if (head->val == val) {
//            return head->next;
//        }
//
//        ListNode *pre = head;
//        ListNode *cur = head->next;
//        while (cur) {
//            if (cur->val != val) {
//                pre = cur;
//                cur = cur->next;
//            } else {
//                pre->next = cur->next;
//                break;
//            }
//        }
//        return head;
        if(!head){
            return NULL;
        }

        ListNode *cur = head;
        ListNode *pre = head;
        while(cur){
            if(cur->val == val){
                ListNode *next = cur->next;
                if(next){
                    cur->val = next->val;
                    cur->next = next->next;
                } else {
                    cur = NULL;
                }
            } else {
                pre = cur;
                cur = cur->next;
            }
        }
        return head;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    ListNode *head = stringToListNode("[-3,5,-99]");
    head = Solution().deleteNode(head,  -99);
    return 0;
}


if(!head){
           return NULL;
       }

       ListNode *cur = head;
       while(cur){
           if(cur->val == val){
               ListNode *next = cur->next;
               if(next){
                   cur->val = next->val;
                   cur->next = next->next;
               } else {
                   cur = NULL;
               }
           } else {
               cur = cur->next;
           }
       }
       return head; if(!head){
           return NULL;
       }

       ListNode *cur = head;
       while(cur){
           if(cur->val == val){
               ListNode *next = cur->next;
               if(next){
                   cur->val = next->val;
                   cur->next = next->next;
               } else {
                   cur = NULL;
               }
           } else {
               cur = cur->next;
           }
       }
       return head;
