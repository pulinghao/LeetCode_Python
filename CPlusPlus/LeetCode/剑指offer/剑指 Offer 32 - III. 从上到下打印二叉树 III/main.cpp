//
//  main.cpp
//  剑指 Offer 32 - III. 从上到下打印二叉树 III
//
//  Created by pulinghao on 2022/6/12.
//

#include <iostream>
#include "common.h"

class A
{
public:
    int i;
    A(int t) :i(t) { cout << "A()" << endl; }
    A(const A&a) :i(a.i) { cout << "拷贝构造" << endl; }
    A( A&&a) :i(a.i) { cout << "移动构造" << endl; }
};

int main()
{
    A a(1);
    vector<A> v1;
    v1.push_back(a);

    cout << "---------------" << endl;

    vector<A> v11;
    v11.push_back(A(2));

    cout << "---------------" << endl;

    vector<A> v2;
    v2.emplace_back(A(3));

    cout << "---------------" << endl;

    vector<A> v22;
    A aa(1);
    v22.emplace_back(aa);

    cout << "---------------" << endl;

    vector<A> v3;
    v3.emplace_back(11); //区别，这里直接传了构造函数的参数
    cout << "---------------" << endl;

    return 0;
}

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(!root) return res;
        deque<TreeNode *> queue;
        queue.push_back(root);
        bool re = true;
        while(!queue.empty()){
            deque<TreeNode *> tempQ;
            vector<int> temp;
            for (int i = 0; i < queue.size(); i++) {
                TreeNode *node = queue.front();
                queue.pop_front();
                temp.push_back(node->val);
                
                if (node->left) {
                    tempQ.push_back(node->left);
                }
                if (node->right) {
                    tempQ.push_back(node->right);
                }
            }
            queue = tempQ;
            if (re) {
                reverse(temp.begin(),temp.end());
            }
            re = !re;
            res.push_back(temp);
        }
        return res;
    }
};
//
//int main(int argc, const char * argv[]) {
//    // insert code here...
////    TreeNode *root = stringtoTre
//    std::cout << "Hello, World!\n";
//    return 0;
//}
