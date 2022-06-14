//
//  main.cpp
//  剑指 Offer 34. 二叉树中和为某一值的路径
//
//  Created by pulinghao on 2022/6/13.
//

#include <iostream>
#include "common.h"

class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> pathSum(TreeNode* root, int target) {
        vector<int> path;
        int sum = 0;
        findPath(root, sum, target, path);
        return res;
    }

    void findPath(TreeNode *node, int sum, int target, vector<int> &path){
        sum += sum;
        path.push_back(node->val);
        if(sum == target){
            res.push_back(path);
        }

        if(node->left){
            findPath(node->left,sum,target,path);
        }

        if(node->right){
            findPath(node->right,sum,target,path);
        }

        path.pop_back();
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string root = "[5,4,8,11,null,13,4,7,2,null,null,5,1]";
//    string root = "[1,null,2]";
    TreeNode *node = stringToTreeNode(root);
    string nodeStr = treeNodeToString(node);
    std::cout << nodeStr<<endl;
    return 0;
}
