//
//  main.cpp
//  剑指 Offer 43. 1～n 整数中 1 出现的次数
//
//  Created by pulinghao on 2022/6/19.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    int countDigitOne(int n) {
        // 以百位的1为例
        int k = 0;
        int res = 0;
        int l = n;
        while(l){
            res += countDigitOneOnK(n, k);
            k++;
            l = l / 10;
        }
        return res;
    }
    
    
    /// <#Description#>
    /// @param n <#n description#>
    /// @param k 表示第几位
    int countDigitOneOnK(int n, int k){
        int res = 0;
        int a = pow(10,k + 1);
        int b = pow(10,k);
        int high = n / a;
        // 有多少个完整的1
        res += b * high;
        int low = n % a;
        if (low < b) {
            res += 0;
        } else if (low < 2 * b){
            res += low - b + 1;
        } else {
            res += b;
        }
        return res;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cout << Solution().countDigitOne(13);
    return 0;
}
