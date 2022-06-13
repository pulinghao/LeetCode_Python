//
//  main.cpp
//  剑指 Offer 26. 树的子结构
//
//  Created by pulinghao on 2022/6/12.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        
        if (!A) {
            return false;
        }
        
        if (!B) {
            return true;
        }
        
        if (A->val == B->val) {
            return isSubStructure(A->left, B->left) || isSubStructure(A->right, B->right);
        } else {
            return isSubStructure(A->left, B) || isSubStructure(A->right, B);
        }
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
