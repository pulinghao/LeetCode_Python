//
//  main.cpp
//  1518. 换酒问题
//
//  Created by pulinghao on 2021/12/17.
//

#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

#include <algorithm>
#include <cmath>

using namespace::std;
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;
        while (numBottles / numExchange != 0) {
            ans += numBottles / numExchange;
            int rest = numBottles / numExchange;
            rest += numBottles % numExchange;
            numBottles = rest;
        }
        return ans;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    int numBottles = 2, numExchange = 3;
    std::cout << Solution().numWaterBottles(numBottles, numExchange)<<endl;
    return 0;
}
