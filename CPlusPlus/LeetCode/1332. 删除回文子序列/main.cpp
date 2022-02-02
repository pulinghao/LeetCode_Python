//
//  main.cpp
//  1332. 删除回文子序列
//
//  Created by pulinghao on 2022/1/22.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    int removePalindromeSub(string s) {
        string revs = s;
        reverse(revs.begin(), revs.end());
        if (revs == s) {
            return 1;
        }
        return 2;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
