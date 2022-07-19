//
//  main.cpp
//  735. 行星碰撞
//
//  Created by pulinghao on 2022/7/13.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;
        for (auto as : asteroids) {
            if (st.empty()) {
                st.push(as);
            } else {
                int top = st.top();
                if (top > 0) {
                    if (as < 0){
                        if (top + as < 0) {
                            while(!st.empty() && st.top() + as < 0 && st.top() > 0){
                                st.pop();
                            }
                            
                            if (st.empty()) {
                                st.push(as);
                            } else {
                                if (st.top() < 0) {
                                    st.push(as);
                                } else {
                                    if (st.top() + as == 0) {
                                        st.pop();
                                    }
                                }
                            }
                        } else if(top + as == 0){
                            st.pop();
                        } else {
                            continue;
                        }
                    } else {
                        st.push(as);
                    }
                } else {
                    st.push(as);
                }
            }
        }
        
        vector<int> res;
        while (!st.empty()) {
            int top = st.top();
            res.push_back(top);
            st.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> asteroids = {1,-2,-2,-2};
    vector<int> res = Solution().asteroidCollision(asteroids);
    return 0;
}
