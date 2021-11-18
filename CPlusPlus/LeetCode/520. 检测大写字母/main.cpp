//
//  main.cpp
//  520. 检测大写字母
//
//  Created by pulinghao on 2021/11/13.
//

#include <iostream>



#include <unordered_map>
#include <string>
#include <vector>

#include <algorithm>

using namespace::std;

class Solution {
public:
    bool detectCapitalUse(string word) {
        size_t length = word.size();
        if (length == 1) {
            return true;
        }
        
        if (isupper(word[0])) {
            // 首字母大写
            if (length == 2) {
                return true;
            } else {
                if (isupper(word[1])) {
                    for (int i = 2; i < length; i++) {
                        char c = word[i];
                        if (islower(c)) {
                            return false;
                        }
                    }
                } else {
                    for (int i = 2; i < length; i++) {
                        char c = word[i];
                        if (isupper(c)) {
                            return false;
                        }
                    }
                }
            }
        } else {
            // 看看后续字母是否都是小写
            for (int i = 0; i < length; i++) {
                char c = word[i];
                if (isupper(c)) {
                    return false;
                }
            }
        }
        return true;
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << Solution().detectCapitalUse("QmO");
    return 0;
}
