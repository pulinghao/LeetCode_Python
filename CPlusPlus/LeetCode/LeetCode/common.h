//
//  common.h
//  LeetCode
//
//  Created by pulinghao on 2021/6/4.
//

#ifndef common_h
#define common_h

#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <numeric>


using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};


/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
 

int stringToInteger(string input) {
    return stoi(input);
}

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

vector<vector<int>> stringToIntegerVectors(string input){
    vector<vector<int>> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    
    string tempStr;
    stack<char> st;
    for (int i = 0; i < input.size(); i++) {
        if (input[i] == '[') {
            tempStr.push_back(input[i]);
        } else if(isnumber(input[i])){
            tempStr.push_back(input[i]);
        } else if(input[i] == ']'){
            tempStr.push_back(input[i]);
            vector<int> outLine = stringToIntegerVector(tempStr);
            output.push_back(outLine);
            tempStr.clear();
        } else {
            if (input[i] == ',') {
                if (tempStr.size() == 0) {
                    continue;
                } else {
                    tempStr.push_back(input[i]);
                }
            }
        }
    }
    
    return output;
}

ListNode* stringToListNode(string input) {
    // Generate list from the input
    vector<int> list = stringToIntegerVector(input);

    // Now convert that list into linked list
    ListNode* dummyRoot = new ListNode(0);
    ListNode* ptr = dummyRoot;
    for(int item : list) {
        ptr->next = new ListNode(item);
        ptr = ptr->next;
    }
    ptr = dummyRoot->next;
    delete dummyRoot;
    return ptr;
}

ListNode* vectorToListNode(vector<int> list){
    ListNode* dummyRoot = new ListNode(0);
    ListNode* ptr = dummyRoot;
    for(int item : list) {
        ptr->next = new ListNode(item);
        ptr = ptr->next;
    }
    ptr = dummyRoot->next;
    delete dummyRoot;
    return ptr;
}



TreeNode *vectorToTreeNode(vector<string> input){
    if (input.size() == 0) {
        return NULL;
    }

    TreeNode *root = (TreeNode *)malloc(sizeof(TreeNode));
    root->val = stringToInteger(input[0]);
    
    deque<TreeNode *> queue;
    int index = 1;
    int front = 0;
    queue.push_back(root);
    while(index < input.size()){
        TreeNode *node = queue[front];
        front += 1;
        string value = input[index];
        index += 1;
        if (value != "#") {
            int leftValue = stringToInteger(value);
            TreeNode *p = new TreeNode();
            p->val = leftValue;
            node->left = p;
            queue.push_back(node->left);
        } else {
            node->left = NULL;
        }
        
        if (index >= input.size()){
            break;
        }
        
        value = input[index];
        index += 1;
        if (value != "#") {
            int rightValue = stringToInteger(value);
            TreeNode *p = new TreeNode();
            p->val = rightValue;
            node->right = p;
            queue.push_back(node->right);
        } else {
            node->right = NULL;
        }
    }
    return root;
}


TreeNode *stringToTreeNode(string input){
    string subString = input.substr(1, input.size() - 2);
    vector<string> arr;
    int start = 0;
    for (int i = 0; i < subString.size(); i++) {
        if (subString[i] == ',') {
            string tempSub = subString.substr(start,i - start);
            if (tempSub == "null") {
                arr.push_back("#");
            } else {
                arr.push_back(tempSub);
            }
            start = i + 1;
        }
    }
    
    string tempSub = subString.substr(start,subString.size() - start);
    if (tempSub == "null") {
        arr.push_back("#");
    } else {
        arr.push_back(tempSub);
    }
    
    return vectorToTreeNode(arr);
}

string treeNodeToString(TreeNode *root){
    string res;
    if (!root) {
        return "[]";
    }
    
    deque<TreeNode *> queue;
    queue.push_back(root);
    while(!queue.empty()){
        TreeNode *front = queue.front();
        
        queue.pop_front();
        if (front) {
            int val = front->val;
            res.append(to_string(val));
            res += ", ";
        } else {
            res += "null, ";
        }
        
        if (front) {
            queue.push_back(front->left);
            queue.push_back(front->right);
        }
    }
    return "[" + res.substr(0,res.length() - 2) + "]";
}


string listNodeToString(ListNode* node) {
    if (node == nullptr) {
        return "[]";
    }

    string result;
    while (node) {
        result += to_string(node->val) + ", ";
        node = node->next;
    }
    return "[" + result.substr(0, result.length() - 2) + "]";
}

#endif /* common_h */
