//
//  main.cpp
//  919. 完全二叉树插入器
//
//  Created by pulinghao on 2022/7/25.
//

#include <iostream>
#include "common.h"

class CBTInserter {
    deque<TreeNode *> q;
    TreeNode *root;
public:
    CBTInserter(TreeNode* root) {
        this->root = root;
        deque<TreeNode *> temp;
        temp.push_back(root);
        while(!temp.empty()){
            TreeNode *top = temp.front();
            temp.pop_front();
            if (top->left) {
                temp.push_back(top->left);
            }
            
            if (top->right) {
                temp.push_back(top->right);
            }
            
            if (top->right == nullptr || top->left == nullptr) {
                // 找到可以插入的节点
                q.push_back(top);
            }
        }
    }
    
    int insert(int val) {
        TreeNode *node = new TreeNode(val);
        TreeNode *top = q.front();
        if (!top->left) {
            top->left = node;
        } else if (!top->right){
            top->right = node; //插入右节点后，就满了
            q.pop_front();
        }
        q.push_back(node);
        return top->val;
    }
    
    TreeNode* get_root() {
        return root;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
