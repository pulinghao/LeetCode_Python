//
//  main.cpp
//  33. 搜索旋转排序数组
//
//  Created by pulinghao on 2022/6/10.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while(left <= right){
            int mid = (left + right) / 2;
            if (target == nums[mid]) {
                return mid;
            } else {
                if (nums[mid] < nums[right]) {
                    // 右边递增
                    if (target > nums[right]) {
                        // 在左边
                        right = mid - 1;
                    } else {
                        if (target > nums[mid]) {
                            left = mid + 1;
                        } else {
                            right = mid - 1;
                        }
                    }
                } else {
                    if (nums[mid] > nums[left]) {
                        // 左边递增
                        if (target < nums[left]) {
                            // 在右边
                            left = mid + 1;
                        } else {
                            if (target > nums[mid]) {
                                left = mid + 1;
                            } else {
                                right = mid - 1;
                            }
                        }
                    } else {
                        if (target > nums[mid]) {
                            right = mid - 1;
                        } else {
                            left = mid + 1;
                        }
                    }
                }
            }
        }
        return -1;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[3,5,1]";
    vector<int> v = stringToIntegerVector(input);
    std::cout << Solution().search(v, 3);
    return 0;
}
