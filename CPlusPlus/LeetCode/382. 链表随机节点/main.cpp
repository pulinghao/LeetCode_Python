//
//  main.cpp
//  382. 链表随机节点
//
//  Created by pulinghao on 2022/1/16.
//

#include <iostream>

#include "common.h"
class Solution {
private:
    int count = 0;
    vector<ListNode *> nodelist;
public:
    Solution(ListNode* head) {
        ListNode *cur = head;
        while (cur) {
            count += 1;
            nodelist.push_back(cur);
            cur = cur->next;
        }
    }
    
    int getRandom() {
        int index = rand() % count;
        ListNode *node = nodelist[index];
        return node->val;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << Solution().getRandom();
    return 0;
}
