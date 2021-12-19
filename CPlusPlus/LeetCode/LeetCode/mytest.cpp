//
//  mytest.cpp
//  LeetCode
//
//  Created by pulinghao on 2021/6/4.
//

#include "mytest.hpp"
#include "common.h"
#include <iostream>
#include <string>
#include <vector>

using namespace::std;
extern int stringToInteger(string input);
extern ListNode* stringToListNode(string input);

using namespace::std;
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *myNode;
        return myNode;
    }
};



//int main() {
//    string line;
//    while (getline(cin, line)) {
//        int intersectVal = stringToInteger(line);
//        getline(cin, line);
//        ListNode* listA = stringToListNode(line);
//        getline(cin, line);
//        ListNode* listB = stringToListNode(line);
//        getline(cin, line);
//        int skipA = stringToInteger(line);
//        getline(cin, line);
//        int skipB = stringToInteger(line);
//        
//        ListNode* ret = Solution().getIntersectionNode(listA,listB);
//
//        string out = listNodeToString(ret);
//        cout << out << endl;
//    }
//    return 0;
//}
