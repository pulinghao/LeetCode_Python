//
//  main.cpp
//  496. 下一个更大元素I
//
//  Created by pulinghao on 2021/10/26.
//

#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        size_t length = nums2.size();
        vector<int> array = vector<int>(length);
        int max = -1;
        for (int i = length - 1; i >= 0; i--) {
            if (nums2[i] > max) {
                array[i] = nums2[i];
                max = nums2[i];
            }
        }
        
        vector<int> ans;
        for (int i = 0; i < nums1.size(); i++) {
            if (nums1[i] > array[i]) {
                ans.push_back(array[i]);
            } else {
                ans.push_back(-1);
            }
        }
        
        return ans;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

string integerVectorToString(vector<int> list, int length = -1) {
    if (length == -1) {
        length = list.size();
    }

    if (length == 0) {
        return "[]";
    }

    string result;
    for(int index = 0; index < length; index++) {
        int number = list[index];
        result += to_string(number) + ", ";
    }
    return "[" + result.substr(0, result.length() - 2) + "]";
}

int main() {
    string line;
    string line1 = "[4,1,2]";
    string line2 = "[1,3,4,2]";
//    while (getline(cin, line)) {
        vector<int> nums1 = stringToIntegerVector(line1);
//        getline(cin, line);
        vector<int> nums2 = stringToIntegerVector(line2);
        
        vector<int> ret = Solution().nextGreaterElement(nums1, nums2);

        string out = integerVectorToString(ret);
        cout << out << endl;
//    }
    return 0;
}
