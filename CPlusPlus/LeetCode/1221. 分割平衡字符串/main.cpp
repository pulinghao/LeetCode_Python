//
//  main.cpp
//  1221. 分割平衡字符串
//
//  Created by pulinghao on 2021/9/7.
//

#include <iostream>
#include <unordered_map>
#include <string>

using namespace::std;
class Solution {
public:
    int balancedStringSplit(string s) {
        unordered_map<string, int> map;
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i == 0) {
                map.insert(s[i], 1);
            }
            
            
            
        }
        
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
