//
//  main.cpp
//  面试-最长回文字串
//
//  Created by pulinghao on 2022/5/23.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    bool isHuiwen(string s){
        int l = s.size() - 1;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != s[l - i]) {
                return false;
            }
        }
        return true;
    }
    int maxLength(string s){
        int res = 0;
        if (s.size() == 0) {
            return res;
        }
        res = 1;
        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j < s.size(); j++) {
                if (isHuiwen(s.substr(i,j + 1))) {
                    res = max(res, j - i);
                }
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string s = "abcba";
    std::cout << Solution().maxLength(s) <<endl;
    return 0;
}
