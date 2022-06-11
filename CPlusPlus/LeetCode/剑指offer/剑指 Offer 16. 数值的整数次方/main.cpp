//
//  main.cpp
//  剑指 Offer 16. 数值的整数次方
//
//  Created by pulinghao on 2022/6/10.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    double myPow(double x, int n) {
        if(equalToZero(x) && n < 0){
            return 0.0;
        }

        bool negative = false;
        if(n < 0){
            negative = true;
            n = -n;
        }

        double result = quickSquare(x,n);
        if(negative){
            result = 1 / result;
        }
        return result;
    }

    double quickSquare(double x, int n){
        if(n == 0){
            return 1;
        }
        if(n == 1){
            return x;
        }

        if(n % 2){
            return quickSquare(x, n>>1) * quickSquare(x, n>>1) * x;
        } else {
            return quickSquare(x, n>>1) * quickSquare(x, n>>1);
        }
    }
    bool equalToZero(double x){
        if(abs(x - 0.0) < 0.0000001){
            return true;
        }
        return false;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << Solution().myPow(0.00001, 2147483647);
    return 0;
}
