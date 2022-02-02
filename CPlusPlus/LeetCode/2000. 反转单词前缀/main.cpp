//
//  main.cpp
//  2000. 反转单词前缀
//
//  Created by pulinghao on 2022/2/2.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    string reversePrefix(string word, char ch) {
        stack<char> st;
        string res;
        int findIdx = -1;
        for (int i = 0; i < word.size(); i++) {
            if (word[i] == ch) {
                findIdx = i;
                break;
            }
        }
        
        if (findIdx == -1) {
            return word;
        } else {
            for (int i = 0; i <= findIdx; i++) {
                st.push(word[i]);
            }
            while (!st.empty()) {
                char c = st.top();
                res.push_back(c);
                st.pop();
            }
            
            for (int i = findIdx + 1; i < word.size(); i++) {
                res.push_back(word[i]);
            }
            return res;
        }
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
