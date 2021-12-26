//
//  main.cpp
//  1609. 奇偶树
//
//  Created by pulinghao on 2021/12/25.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode *> q;
        q.push(root);

        int level = 0;
        while (!q.empty()) {
            int size = q.size();
            int prev = level % 2 == 0 ? INT_MIN : INT_MAX;
            for (int i = 0; i < size; i++) {
                TreeNode *node = q.front();
                q.pop();
                int value = node->val;
                if (level % 2 == value % 2) {
                    return false;
                }
                if ((level % 2 == 0 && value <= prev) || (level % 2 == 1 && value >= prev)) {
                    return false;
                }

                prev = value;
                if (node->left != nullptr) {
                    q.push(node->left);
                }
                
                if (node->right != nullptr) {
                    q.push(node->right);
                }
            }
            level++;
        }
        return true;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
