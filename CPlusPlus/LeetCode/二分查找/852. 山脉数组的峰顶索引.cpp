#include <iostream>
#include <vector>

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {

    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[3,5,1]";
    vector<int> v = stringToIntegerVector(input);
    std::cout << Solution().search(v, 3);
    return 0;
}