//
//  main.cpp
//  1629. 按键持续时间最长的键
//
//  Created by pulinghao on 2022/1/9.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        unordered_map<char, int> map;
        int maxTime = 0;
        char maxChar = 'a';
        for (int i = 0; i < keysPressed.size(); i++) {
            char c = keysPressed[i];
            int time = 0;
            if (i == 0) {
                time = releaseTimes[0];
                maxChar = c;
            } else {
                time = releaseTimes[i] - releaseTimes[i - 1];
            }
            
            if (time > maxTime) {
                maxChar = c;
                maxTime = time;
            } else if (time == maxTime){
                if (maxChar < c) {
                    maxChar = c;
                }
            }
        }
        return maxChar;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> releaseTimes = {12,23,36,46,62};
    string keysPressed = "spuda";
    
    std::cout << Solution().slowestKey(releaseTimes, keysPressed);
    return 0;
}
