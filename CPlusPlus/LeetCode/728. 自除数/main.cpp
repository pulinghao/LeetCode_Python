//
//  main.cpp
//  728. 自除数
//
//  Created by pulinghao on 2022/3/31.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        for (int i = left; i < right + 1; i++) {
            int num = i;
            bool isRightNum = true;
            while (num != 0) {
                int rest = num % 10;
                if (rest == 0) {
                    isRightNum = false;
                    break;
                }
                if (i % rest == 0) {
                    num = num / 10;
                    continue;
                } else {
                    isRightNum = false;
                    break;
                }
            }
            if (isRightNum) {
                res.push_back(i);
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    int left = 21;
    int right = 22;
    vector<int> res = Solution().selfDividingNumbers(left, right);
    return 0;
}
