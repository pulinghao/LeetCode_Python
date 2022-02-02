//
//  main.cpp
//  2047. 句子中的有效单词数
//
//  Created by pulinghao on 2022/1/27.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int countValidWords(string sentence) {
        int n = sentence.length();
        int l = 0, r = 0;
        int ret = 0;
        string_view slice(sentence);
        while (true) {
            while (l < n && sentence[l] == ' ') {
                l++;
            }
            
            if (l >= n) {
                break;
            }
            
            r = l + 1;
            while (r < n && sentence[r] != ' ') {
                r++;
            }
            
            if (isValid(slice.substr(l, r - l))) {
                ret++;
            }
            l = r + 1;
        }
        return ret;
    }
    
    bool isValid(const string_view &str){
        int n = str.length();
        bool hasgang = false;
        for (int i = 0; i < n ; i++) {
            if (str[i] >= '0' && str[i] <= '9') {
                // 判断条件1，不能是数字
                return false;
            } else if (str[i] == '-'){
                if (hasgang == true || i == 0 || i == n - 1 || !islower(str[i - 1]) || !islower(str[i + 1])) {
                    // 对 - 的条件判断
                    return false;
                }
                hasgang = true;
            } else if (str[i] == '!' || str[i] == '.' || str[i] == ','){
                // 对 ! , . 的判断
                if (i != n - 1) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
