//
//  main.cpp
//  559. N 叉树的最大深度
//
//  Created by pulinghao on 2021/11/21.
//

#include "common.h"
#include <iostream>



// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
public:
    int maxDepth(Node* root) {
        if (!root) {
            return 0;
        }
        int maxV = 0;
        for (int i = 0; i < root->children.size(); i++) {
            Node *child = root->children[i];
            maxV = max(maxDepth(child), maxV);
        }
        return maxV + 1;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

