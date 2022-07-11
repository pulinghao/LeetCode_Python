//
//  main.cpp
//  剑指 Offer 36. 二叉搜索树与双向链表
//
//  Created by pulinghao on 2022/6/27.
//

#include <iostream>
#include "common.h"

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        Node *node = treeToList(root);
        Node *head = node;
        Node *tail = node;
        while(head->left){
            head = head->left;
        }

        while(tail->right){
            tail = tail->right;
        }

        head->left = tail;
        tail->right = head;
        return head;
    }

    Node* treeToList(Node *root){
        if(!root){
            return root;
        }

        Node *leftTree = treeToList(root->left);
        if (leftTree)
        {
            leftTree->right = root;
            root->left = leftTree;
        }
    
        Node *rightTree = treeToList(root->right);
        if (rightTree)
        {
            rightTree->left = root;
            root->right = rightTree;
        }
        return root;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
