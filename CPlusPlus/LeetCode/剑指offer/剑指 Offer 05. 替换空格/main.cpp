//
//  main.cpp
//  剑指 Offer 05. 替换空格
//
//  Created by pulinghao on 2022/6/9.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    string replaceSpace(string s) {
        int count = 0;
        int oldSize = s.size();
        for (int i = 0; i < oldSize; i++) {
            if (s[i] == ' ') {
                count++;
            }
        }
        s.resize(s.size() + count * 2);
        int newSize = s.size();
        
        return s;
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
