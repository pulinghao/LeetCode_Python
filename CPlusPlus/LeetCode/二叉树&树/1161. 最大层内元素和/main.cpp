//
//  main.cpp
//  1161. 最大层内元素和
//
//  Created by pulinghao on 2022/7/31.
//

#include <iostream>
#include "common.h"

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

public:
    int maxLevelSum(TreeNode* root) {
        deque<TreeNode *> queue;
        queue.push_back(root);
        int size = 1;
        int maxSum = -INT_MAX;
        int currentLevel = 0;
        int maxLevel = 0;
         while(!queue.empty()){
            int levelSize = size;
            int sum = 0;
            while(levelSize > 0){
                TreeNode *top = queue.front();
                
                queue.pop_front();
                sum += top->val;
                levelSize--;
                if (top->left) {
                    queue.push_back(top->left);
                }
                
                if (top->right) {
                    queue.push_back(top->right);
                }
            }
            currentLevel++;
            size = queue.size();
            if (sum > maxSum) {
                maxSum = sum;
                maxLevel = currentLevel;
            } else if (sum == maxSum){
                if (currentLevel < maxLevel) {
                    maxLevel = currentLevel;
                }
            }
        }
        return maxLevel;
        
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<string> input = {"1","7","0","7","-8","#","#"};
    TreeNode *root = vectorToTreeNode(input);
    int res = Solution().maxLevelSum(root);
    std::cout << res <<endl;
    return 0;
}
