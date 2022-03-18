//
//  main.cpp
//  599. 两个列表的最小索引总和
//
//  Created by pulinghao on 2022/3/14.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> map1;
        unordered_map<string, int> map2;
        for (int i = 0; i < list1.size(); i++) {
            map1[list1[i]] = i;
        }
        
        for (int i = 0; i < list2.size(); i++) {
            map2[list2[i]] = i;
        }
        
        vector<string> res;
        int index = list1.size() + list2.size();
        if (list1.size() > list2.size()) {
            for (int i = 0; i < list1.size(); i++) {
                if (map2.count(list1[i]) > 0) {
                    if (index > i + map2[list1[i]]) {
                        index = i + map2[list1[i]];
                        res.clear();
                        res.push_back(list1[i]);
                    } else if (index == i + map2[list1[i]]) {
                        res.push_back(list1[i]);
                    }
                }
            }
        } else {
            for (int i = 0; i < list2.size(); i++) {
                if (map1.count(list2[i])> 0) {
                    if (index > i + map1[list2[i]]) {
                        index = i + map1[list2[i]];
                        res.clear();
                        res.push_back(list2[i]);
                    } else if (index == i + map1[list2[i]]) {
                        res.push_back(list2[i]);
                    }
                }
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<string> list1 = {"Shogun","Tapioca Express","Burger King","KFC"};
    vector<string> list2 = {"KFC","Burger King","Tapioca Express","Shogun"};
    vector<string> res =  Solution().findRestaurant(list1, list2);
    return 0;
}
