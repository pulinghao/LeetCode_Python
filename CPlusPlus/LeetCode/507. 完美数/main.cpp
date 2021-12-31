//
//  main.cpp
//  507. 完美数
//
//  Created by pulinghao on 2021/12/31.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num == 1) {
            return false;
        }
        bool res = false;
        int sum = 0;
        float temp = sqrt(num);
        int tempi = int(temp);
        for (int i = 1; i <= tempi; i++) {
            if (num % i == 0) {
                sum += i;
                if (i == 1) {
                    continue;
                } else {
                    sum = sum + num / i;
                }
            }
        }
        
        if (sum == num) {
            res = true;
        }
        return res;
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << Solution().checkPerfectNumber(1)<<endl;
    return 0;
}
