//
//  main.cpp
//  2034. 股票价格波动
//
//  Created by pulinghao on 2022/1/23.
//

#include <iostream>
#include "common.h"

class StockPrice {
private:
    int maxTimeStamp;
    unordered_map<int, int> timePriceMap;
    multiset<int> prices;   //有序列表
public:
    StockPrice() {
        this->maxTimeStamp = 0;
    }
    
    void update(int timestamp, int price) {
        maxTimeStamp = max(maxTimeStamp, timestamp);
        int prePrice = timePriceMap.count(timestamp) > 0 ? timePriceMap[timestamp] : 0;
        timePriceMap[timestamp] = price;
        if (prePrice > 0) {
            auto it = prices.find(prePrice);
            if (it != prices.end()) {
                prices.erase(it); //删除之前的数据
            }
        }
        prices.emplace(price);
    }
    
    int current() {
        return this->timePriceMap[this->maxTimeStamp];
    }
    
    int maximum() {
        return *prices.rbegin();  //返回逆向迭代器，第一个元素，最大元素
    }
    
    int minimum() {
        return *prices.begin();  //最小元素
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
