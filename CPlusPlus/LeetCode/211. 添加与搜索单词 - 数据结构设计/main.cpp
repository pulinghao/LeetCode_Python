//
//  main.cpp
//  211. 添加与搜索单词 - 数据结构设计
//
//  Created by pulinghao on 2022/7/11.
//

#include <iostream>
#include "common.h"

const int maxn = 1e5 + 50;
bool vis[maxn];
int dict[maxn][26];
int idx;

class WordDictionary {
    
public:
    WordDictionary() {
        memset(vis, false, sizeof vis);
        memset(dict, 0, sizeof dict);
        idx = 0;
    }
    
    void addWord(string word) {
        int p = 0;
        for (int i = 0; i < word.length(); i++) {
            int u = word[i] - 'a';
            if (dict[p][u] == 0) {
                ++idx;
                dict[p][u] = idx;
            }
            p = dict[p][u];
        }
        vis[p] = true;
    }
    
    bool search(string word) {
        return dfs(word,0,0);
    }
    
    bool dfs(string s,int trIdx,int sIdx){
        int n = s.length();
        if (sIdx == n) {
            return vis[trIdx];
        }
        
        char c = s[sIdx];
        if (c == '.') {
            for (int j = 0; j < 26; j++) {
                if (dict[trIdx][j] != 0 && dfs(s, dict[trIdx][j], sIdx + 1)) return true;
            }
            return false;
        } else {
            int u = c - 'a';
            if (dict[trIdx][u] == 0) {
                return false;
            }
            return dfs(s, dict[trIdx][u], sIdx + 1);
        }
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    WordDictionary *wordDictionary = new WordDictionary();
//    wordDictionary->addWord("bad");
//    wordDictionary->addWord("dad");
//    wordDictionary->addWord("mad");
//    wordDictionary->search("pad");
//    wordDictionary->search("bad");
//    wordDictionary->search(".ad");
//    wordDictionary->search("b..");
        wordDictionary->addWord("a");
        wordDictionary->addWord("a");
        wordDictionary->addWord(".");
        wordDictionary->search("pad");
        wordDictionary->search("bad");
        wordDictionary->search(".ad");
        wordDictionary->search("b..");
    return 0;
}
