//
//  main.cpp
//  868. 二进制间距（1）
//
//  Created by pulinghao on 2022/4/24.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int binaryGap(int n) {
        int res = 0;
        int count = 0;
        bool hasOne = false;
        while(n){
            int r = n % 2;
            if (r == 1) {
                if (hasOne == false) {
                    hasOne = true;
                } else {
                    res = max(res,count);
                }
                count = 1;
            } else {
                count++;
            }
            n = n / 2;
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    int n =8;
    std::cout << Solution().binaryGap(n)<<endl;
    return 0;
}
