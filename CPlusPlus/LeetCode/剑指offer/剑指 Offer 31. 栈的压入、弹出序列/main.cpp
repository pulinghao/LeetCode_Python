//
//  main.cpp
//  剑指 Offer 31. 栈的压入、弹出序列
//
//  Created by pulinghao on 2022/6/11.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> temp;
        int num = 0;
        for (int i = 0; i < pushed.size(); i++) {
            temp.push(pushed[i]);
            while (!temp.empty() && temp.top() == popped[num]) {
                temp.pop();
                num++;
            }
        }
        return temp.empty() ? true : false;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> push = {1,2,3,4,5};
    vector<int> pop = {4,5,3,2,1};
    
    std::cout<<Solution().validateStackSequences(push, pop);
    return 0;
}
