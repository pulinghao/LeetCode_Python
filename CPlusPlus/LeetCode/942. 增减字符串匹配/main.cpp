//
//  main.cpp
//  942. 增减字符串匹配
//
//  Created by pulinghao on 2022/5/9.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    vector<int> diStringMatch(string s) {
        int n = s.length(), lo = 0, hi = n;
        vector<int> perm(n + 1);
        for (int i = 0; i < n; ++i) {
            perm[i] = s[i] == 'I' ? lo++ : hi--;
        }
        perm[n] = lo; // 最后剩下一个数，此时 lo == hi
        return perm;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string s = "III";
    vector<int> res = Solution().diStringMatch(s);
    
    std::cout << "Hello, World!\n";
    return 0;
}
