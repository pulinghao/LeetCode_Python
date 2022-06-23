//
//  main.cpp
//  LeetCode
//
//  Created by pulinghao on 2021/6/4.
//

#include <iostream>


#include "common.h"

/*
 max_element()
 */

vector<int> getLeastNumbers(vector<int>& arr, int k) {
        vector<int> res;
        int start = 0;
        int end = arr.size() - 1;
        int index = partion(arr,start,end);
        while(index != k - 1){
            if(index < k - 1){
                start = index + 1;
                index = partion(arr,start,end);
            } else {
                end = index - 1;
                index = partion(arr,start,end);
            }
        }
        for(int i = 0; i < k; i++){
            res.push_back(arr[i]);
        }
        return res;
    }

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> k{ 1,2,3 };
    vector<int> q;
    vector<int>* p;
    vector<int>* qq;
    shared_ptr<vector<int>> sp;
//    vector<int>* p;
//    p = &k;
    for (int i = 0; i < 3; i++) {
        vector<int> temp;
        temp.push_back(i + 1);
        p = &temp;
        q = temp;
        qq = &q;
        
       
    }
    
    cout<<p->at(0);
    
    p->push_back(4);
    for (int i = 0; i < p->size(); i++)
    {
        cout << p->at(i) << ' ';
    }
    
    //1 1 1

    cout<<endl;
    return 0;
}
