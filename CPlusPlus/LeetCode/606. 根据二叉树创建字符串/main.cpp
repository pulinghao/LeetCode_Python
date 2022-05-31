//
//  main.cpp
//  606. 根据二叉树创建字符串
//
//  Created by pulinghao on 2022/3/19.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    string tree2str(TreeNode* root) {
        string res;
        if (root) {
            res += to_string(root->val);
        }
        
        if (root->left) {
            res += "(";
            res += tree2str(root->left);
            res += ")";
        } else {
            if (root->right) {
                res += "(";
                res += ")";
            }
        }
        
        
        
        if (root->right) {
            res += "(";
            res += tree2str(root->right);
            res += ")";
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
