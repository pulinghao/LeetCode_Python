//
//  main.cpp
//  1005. K 次取反后最大化的数组和
//
//  Created by pulinghao on 2021/12/3.
//

#include <iostream>

#include <string>
#include <vector>
#include <sstream>
#include <math.h>

using namespace::std;

class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        vector<int> array1;
        vector<int> array2;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] >= 0) {
                array1.push_back(nums[i]);
            } else {
                array2.push_back(nums[i]);
            }
        }
        
        sort(array1.begin(), array1.end());
        sort(array2.begin(), array2.end());
        
        int res = 0;
        if (array2.size() >= k) {
            for (int i = 0; i < k; i++) {
                array2[i] = array2[i] * (-1);
            }
            
            
            for (int i = 0; i < array1.size(); i++) {
                res += array1[i];
            }
            
            for (int j = 0; j < array2.size(); j++) {
                res += array2[j];
            }
        } else {
            for (int i = 0; i < array2.size(); i++) {
                array2[i] = array2[i] * (-1);
            }
            vector<int> array3;
            for (int i = 0; i < array1.size(); i++) {
                array3.push_back(array1[i]);
            }
            
            for (int j = 0; j < array2.size(); j++) {
                array3.push_back(array2[j]);
            }
            
            sort(array3.begin(), array3.end());
            for (int i = 1; i < array3.size(); i++) {
                res += array3[i];
            }
            
            int rest = k - (int)array2.size();
            res += array3[0] * pow(-1, rest);
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
