//
//  main.cpp
//  1078. Bigram 分词
//
//  Created by pulinghao on 2021/12/26.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        vector<string> list;
        string temp = "";
        for (int i = 0; i < text.size(); i++) {
            if (text[i] != ' ') {
                temp += text[i];
            } else {
                list.push_back(temp);
                temp = "";
            }
        }
        
        list.push_back(temp);
        
        vector<string> res;
        for (int i = 0; i < list.size(); i++) {
            string idxi = list[i];
            if (idxi == first) {
                if (i + 1 < list.size()) {
                    if (list[i + 1] == second) {
                        if (i + 2 < list.size()) {
                            res.push_back(list[i + 2]);
                        }
                    }
                }
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string text = "alice is a good girl she is a good student";
    string first = "a";
    string second = "good";

    vector<string> res = Solution().findOcurrences(text,first,second);
    return 0;
}
