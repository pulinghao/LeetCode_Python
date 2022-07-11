//
//  main.cpp
//  剑指 Offer 28. 对称的二叉树
//
//  Created by pulinghao on 2022/6/21.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) {
            return false;
        }
        return checkTreeEqual(root->left, root->right);
    }
    
    bool checkTreeEqual(TreeNode *p, TreeNode *q){
        if ((!p && q) || (p && !q)) {
            return false;
        }
        
        if (!p && !q) {
            return true;
        }
        
        if (p->val != q->val) {
            return false;
        }
        
        return (p->val == q->val) && checkTreeEqual(p->left, q->right) && checkTreeEqual(p->right, q->left);
    }
};



int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[1,2,2,3,4,4,3]";
    TreeNode *node = stringToTreeNode(input);
    std::cout << Solution().isSymmetric(node);
    return 0;
}
