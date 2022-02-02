//
//  main.cpp
//  884. 两句话中的不常见单词
//
//  Created by pulinghao on 2022/1/30.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> map1;
        unordered_map<string, int> map2;
        string ss1;
        string ss2;
        for (int i = 0; i < s1.length(); i++) {
            if (s1[i] == ' ') {
                map1[ss1]++;
                ss1.clear();
            } else {
                ss1.push_back(s1[i]);
            }
        }
        map1[ss1]++;
        
        for (int i = 0; i < s2.length(); i++) {
            if (s2[i] == ' ') {
                map2[ss2]++;
                ss2.clear();
            } else {
                ss2.push_back(s2[i]);
            }
        }
        map2[ss2]++;
        vector<string> res;
        for (auto iter = map1.begin(); iter != map1.end(); ++iter) {
            string key = iter->first;
            int value = iter->second;
            if (value > 1) {
                continue;
            } else {
                if (map2.count(key) == 0) {
                    res.push_back(key);
                }
            }
        }
        
        for (auto iter = map2.begin(); iter != map2.end(); ++iter) {
            string key = iter->first;
            int value = iter->second;
            if (value > 1) {
                continue;
            } else {
                if (map1.count(key) == 0) {
                    res.push_back(key);
                }
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string s1 = "this is an apple";
    string s2 = "this is an orange";
    vector<string> res = Solution().uncommonFromSentences(s1, s2);
    return 0;
}
