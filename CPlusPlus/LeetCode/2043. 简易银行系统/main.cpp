//
//  main.cpp
//  2043. 简易银行系统
//
//  Created by pulinghao on 2022/3/18.
//

#include <iostream>
#include "common.h"

class Bank {
private:
    vector<long long> balances;
public:
//    Bank(vector<long long>& balance) : balances(balance) {}
    Bank(vector<long long>& balance) {
        balances.push_back(-1);
        for (int i = 0; i < balance.size(); i++) {
            long long num = balance[i];
            balances.push_back(num);
        }
    }
    
    bool transfer(int account1, int account2, long long money) {
        if (account1 >= balances.size() || account2 >= balances.size()) {
            return false;
        }
        
        if (balances[account1] < money) {
            return false;
        }
        
        balances[account1] -= money;
        balances[account2] += money;
        return true;
    }
    
    bool deposit(int account, long long money) {
        if (account >= balances.size()) {
            return false;
        }
        
        balances[account] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if (account < balances.size()) {
            if (balances[account] >= money) {
                balances[account] -= money;
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<long long> v = {0};
    Bank* obj = new Bank(v);
//    bool param_1 = obj->withdraw(3,10);
//    bool param_2 = obj->transfer(5,1,20);
    bool param_3 = obj->deposit(1,1000000000000);
    bool param_4 = obj->transfer(1,1,1000000000000);
    bool param_5 = obj->withdraw(1,1000000000000);
    return 0;
}
