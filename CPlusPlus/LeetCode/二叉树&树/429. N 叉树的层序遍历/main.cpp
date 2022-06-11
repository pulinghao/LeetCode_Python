//
//  main.cpp
//  429. N 叉树的层序遍历
//
//  Created by pulinghao on 2022/4/8.
//

#include <iostream>
#include "common.h"



class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        if (!root) {
            return {};
        }
        
        queue<Node *> q;
        q.push(root);
        while (!q.empty()) {
            int cnt = q.size();
            vector<int> level;
            for (int i = 0; i < cnt; i++) {
                Node *cur = q.front();
                level.push_back(cur->val);
                for (Node *child : cur->children) {
                    q.push(child);
                }
            }
            res.push_back(level);
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}


