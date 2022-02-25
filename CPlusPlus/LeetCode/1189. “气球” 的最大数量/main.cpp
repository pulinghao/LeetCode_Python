//
//  main.cpp
//  1189. “气球” 的最大数量
//
//  Created by pulinghao on 2022/2/13.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> dict = {{'b',0},{'a',0},{'l',0},{'o',0},{'n',0}};
        for (auto &c : text){
            if (c == 'b' || c == 'a' || c =='l' || c == 'o' || c == 'n') {
                dict[c]++;
            }
        }
        
        char  minChar = 'b';
        int count = text.size();
        for (auto iter = dict.begin(); iter != dict.end(); ++iter) {
            int showCount = iter->second;
            if (iter->first == 'l' || iter->first == 'o') {
                showCount = showCount / 2;
            }
            if (count > showCount) {
                count = showCount;
                minChar = iter->first;
            }
        }
        return count;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string text = "leetcode";
    std::cout << Solution().maxNumberOfBalloons(text)<<endl;
    return 0;
}
