//
//  main.cpp
//  LeetCode
//
//  Created by pulinghao on 2021/6/4.
//

#include <iostream>

#include <stdio.h>
#include <stdlib.h>



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
//    string s = "abcde";
//    cout<<s.substr(0,1);
//    int start = 3;
//    int end = 6;
//    cout<<endl;
//    return 0;
    char str[30] = "e";
    char *ptr;
    long ret;

    ret = strtoul(str, 0, 16);
    printf("数字（无符号长整数）是 %lu\n", ret);
    printf("字符串部分是 |%s|\n", ptr);

    return(0);
}
