//
//  main.cpp
//  2038. 如果相邻两个颜色均相同则删除当前颜色
//
//  Created by pulinghao on 2022/3/22.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    bool winnerOfGame(string colors) {
        int freq[2] = {0, 0};
        char cur = 'C';
        int cnt = 0;
        for (char c : colors) {
            if (c != cur) {
                cur = c;
                cnt = 1;
            } else if (++cnt >= 3) {
                ++freq[cur - 'A'];
            }
        }
        return freq[0] > freq[1];
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << Solution().winnerOfGame("BBAAABBABBABB");
    return 0;
}
