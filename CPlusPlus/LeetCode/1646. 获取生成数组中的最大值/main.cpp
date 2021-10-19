//
//  main.cpp
//  1646. 获取生成数组中的最大值
//
//  Created by pulinghao on 2021/8/23.
//

#include <iostream>

#include <vector>
#include <algorithm>

using namespace::std;
class Solution {
public:
    int getMaximumGenerated(int n) {
        vector<int> array;
        
        for (int i = 0; i < n + 1; i++) {
            if (i == 0 ) {
                array.push_back(0);
            }
            if (i == 1) {
                array.push_back(1);
            }
            
            if (i > 1) {
                if (i % 2 == 1) {
                    int temp1 = i / 2;
                    int temp2 = i / 2 + 1;
                    int temp3 = array[temp1] + array[temp2];
                    array.push_back(temp3);
                }
                
                if (i % 2 == 0) {
                    int temp1 = i / 2;
                    array.push_back(array[temp1]);
                }
            }
            
        }
        vector<int>::iterator max = max_element(begin(array), end(array));
        int value = *max;
        return value;
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    Solution so;
    cout<<so.getMaximumGenerated(7)<<endl;
    return 0;
}
