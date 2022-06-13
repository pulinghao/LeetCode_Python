//
//  main.cpp
//  剑指 Offer 54. 二叉搜索树的第k大节点
//
//  Created by pulinghao on 2022/6/12.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    int res;
    int kthLargest(TreeNode* root, int k) {
        //
        dfs(root,k);
        return res;
    }
    
    void dfs(TreeNode *node,int &k){
        if (!node) {
            return;
        }
        
        dfs(node->right,k);
        k--;
        if (k == 0) {
            res = node->val;
        }
        dfs(node->left,k);
    }
    
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
