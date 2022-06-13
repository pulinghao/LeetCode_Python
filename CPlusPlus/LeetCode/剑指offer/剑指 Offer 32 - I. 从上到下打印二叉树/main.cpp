//
//  main.cpp
//  剑指 Offer 32 - I. 从上到下打印二叉树
//
//  Created by pulinghao on 2022/6/12.
//

#include <iostream>
#include "common.h"
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
        vector<int> res;
        deque<TreeNode *> queue;
        if(!root) return res;
        stack<int> st;
        queue.push_back(root);
        while(!queue.empty()){
            TreeNode *node = queue.front();
            
            queue.pop_front();
            res.push_back(node->val);
            if(node->left){
                queue.push_back(node->left);
            }

            if(node->right){
                queue.push_back(node->right);
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
