//
//  main.cpp
//  1614. 括号的最大嵌套深度
//
//  Created by pulinghao on 2022/1/7.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    int maxDepth(string s) {
        vector<char> stack;
        int res = 0;
        for(auto c : s){
            if (c == '(') {
                stack.push_back(c);
//                res = max(res, stack.size());
                int size = stack.size();
                res = max(res, size);
            } else if (c == ')'){
                stack.pop_back();
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string s = "(1+(2*3)+((8)/4))+1";
    std::cout << Solution().maxDepth(s)<<endl;
    return 0;
}
