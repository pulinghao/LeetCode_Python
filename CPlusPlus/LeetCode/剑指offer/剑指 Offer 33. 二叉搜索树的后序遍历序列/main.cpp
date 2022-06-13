//
//  main.cpp
//  剑指 Offer 33. 二叉搜索树的后序遍历序列
//
//  Created by pulinghao on 2022/6/13.
//

#include <iostream>
#include "common.h"
class Solution {
public:
    bool verifyPostorder(vector<int>& postorder) {
        if(postorder.size() == 0){
            return false;
        }
        int length = postorder.size();
        int root = postorder[length - 1];
        int i = 0;
        vector<int> left_v;
        vector<int> right_v;

       
        for(;i < length - 1;i++){
            if(postorder[i] > root){
                break;
            } else {
                left_v.push_back(postorder[i]);
            }
        }
        int j = i;
        for(;j < length - 1;j++){
            if(postorder[j] < root){
                return false;
            } else {
                right_v.push_back(postorder[j]);
            }
        }

        bool left = true;
        if(i > 0){
            left = verifyPostorder(left_v);
        }

        bool right = true;
        if (i < length - 1){
            right = verifyPostorder(right_v);
        }
        return left && right;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> nums = {4, 8, 6, 12, 16, 14, 10};
    std::cout << Solution().verifyPostorder(nums);
    return 0;
}
