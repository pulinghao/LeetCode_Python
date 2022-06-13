//
//  main.cpp
//  890. 查找和替换模式
//
//  Created by pulinghao on 2022/6/12.
//

#include <iostream>


#include "common.h"
class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> res;
        for (string s : words) {
            if (s.size() != pattern.size()) {
                // 长度不同，直接pass
                continue;
            } else {
                unordered_map<char, char> map;
                unordered_map<char, char> map2;
                bool match = true;
                for (int i = 0; i < s.size(); i++) {
                    char wc = s[i];
                    char pc = pattern[i];
                    if (!map[pc]){
                        if (!map2[wc]) {
                            map[pc] = wc;
                            map2[wc] = pc;
                        } else {
                            if (map2[wc]!=pc) {
                                match = false;
                                break;
                            }
                        }
                    } else {
                        if (map[pc] == wc) {
                            if (map2[wc] != pc) {
                                match = false;
                                break;
                            } else {
                                continue;
                            }
                        } else {
                            match = false;
                            break;
                        }
                    }
                }
                if (match) {
                    res.push_back(s);
                }
            }
        }
        return res;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    vector<string> words = {"abc","deq","mee","aqq","dkd","ccc"};
//    vector<string> words = {"ccc"};
    string pattern = "abb";
    vector<string> res = Solution().findAndReplacePattern(words, pattern);
    return 0;
}
