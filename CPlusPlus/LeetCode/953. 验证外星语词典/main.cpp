#include "common.h"

class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        unordered_map<char, int> mapping;
        for (int i = 0; i < order.size(); ++i) {
            mapping[order[i]] = i;
        }
        vector<string> decrypt;
        for (string& word : words) {
            string decryptWord;
            for (char c : word) {
                decryptWord += 'a' + mapping[c];
            }
            decrypt.push_back(decryptWord);
        }
        return is_sorted(decrypt.begin(), decrypt.end());
    }
};