//
//  main.cpp
//  1089. 复写零
//
//  Created by pulinghao on 2022/6/17.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int count = 0;
        int size = 0;
        while(count < arr.size()){
            if(arr[size] == 0){
                count += 2;
            } else {
                count++;
            }
            size++;
        }

        int i = INT_MAX;
        int j = arr.size() - 1;
        int i = size - 1;
        if (count == arr.size() + 1) {
            arr[j] = 0;
            j--;
            i--;
        }
        while(i >= 0){
            arr[j] = arr[i];
            j--;
            if (arr[i] == 0) {
                arr[j] = arr[i];
                j--;
            }
            i--;
        }
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> arr = {0,0,0,0,0,0,0};
    Solution().duplicateZeros(arr);
    return 0;
}
