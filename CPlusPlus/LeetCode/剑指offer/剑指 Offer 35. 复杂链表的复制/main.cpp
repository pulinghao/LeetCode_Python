//
//  main.cpp
//  剑指 Offer 35. 复杂链表的复制
//
//  Created by pulinghao on 2022/6/16.
//

#include <iostream>
//#include "common.h"

class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        cloneNode(head);
        connectRandomNode(head);
        return construct(head);
    }
    
    void cloneNode(Node *node){
        Node *cur = node;
        while(cur){
            Node *pClone = new Node(0);
            pClone->val = cur->val;
            pClone->next = cur->next;
            pClone->random = NULL;
            cur = pClone->next;
        }
    }
    
    void connectRandomNode(Node *node){
        Node *cur = node;
        while (cur) {
            Node *pClone = cur->next;
            if(cur->random){
                Node *randomeNode = cur->random;
                pClone->random = randomeNode->next;
            }
            cur = pClone->next;
        }
    }
    
    Node* construct(Node *node){
        Node *head = NULL;
        if (node->next) {
            head = node->next;
        }
        
        Node *cur = head;
        while (cur) {
            if (cur->next && cur->next->next) {
                cur->next = cur->next->next;
                cur = cur->next;
            }
        }
        return head;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cout << "Hello, World!\n";
    return 0;
}
