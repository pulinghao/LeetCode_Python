//
//  main.cpp
//  1446. 连续字符
//
//  Created by pulinghao on 2021/12/1.
//

#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

#include <algorithm>
using namespace::std;

class Solution {
public:
    int maxPower(string s) {
        int i = 0;
        int j = 0;
        int res = 0;
        
        for (j = 0; j < s.length(); j++) {
            if (s[i] == s[j]) {
                continue;
            } else {
                res = max(res, j - i);
                i = j;
            }
        }
        res = max(res, j - i);
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string  s = "c";
    std::cout << Solution().maxPower(s)<<endl;
    return 0;
}
