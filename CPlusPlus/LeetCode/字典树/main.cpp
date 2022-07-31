//
//  main.cpp
//  字典树
//
//  Created by pulinghao on 2022/7/11.
//

#include <iostream>

#include "common.h"
struct TrieTreeNode
{
    bool end;
    std::vector<TrieTreeNode *> children = vector<TrieTreeNode *>(26,nullptr);
};

const int maxn = 1e5 + 50;
bool vis[maxn];
int son[maxn][26],idx;
class Trie {
public:
    Trie() {
        memset(vis,false,sizeof vis);
        memset(son,0,sizeof son);
        idx = 0;
    }
    
    void insert(string word) {
        int p = 0;
        for(auto x : word){
            int u = x - 'a';
            if(!son[p][u]) son[p][u] = ++idx;
            p = son[p][u];
        }
        vis[p] = true;
    }
    
    bool search(string word) {
        int p = 0;
        for(auto x : word){
            int u = x - 'a';
            if(!son[p][u]) return false;
            p = son[p][u];
        }
        return vis[p];
    }
    
    bool startsWith(string prefix) {
        int p = 0;
        for(auto x : prefix){
            int u = x - 'a';
            if(!son[p][u]) return false;
            p = son[p][u];
        }
        return true;
    }
};

//class Trie {
//private:
//    TrieTreeNode *root;
//public:
//    Trie() {
//        root = new TrieTreeNode();
//    }
//
//    void insert(string word) {
//        TrieTreeNode *p = root;
//        for (int i = 0; i < word.length(); ++i)
//        {
//            int u = word[i] - 'a';
//            if (p->children[u] == nullptr)
//            {
//                p->children[u] = new TrieTreeNode();
//            }
//            p = p->children[u];
//        }
//        p->end = true;
//    }
//
//    bool search(string word) {
//        TrieTreeNode *p = root;
//        for (int i = 0; i < word.length(); ++i)
//        {
//            int u = word[i] - 'a';
//            if (p->children[u] == nullptr)
//            {
//                return false;
//            }
//            p = p->children[u];
//        }
//        return p->end;
//    }
//
//    bool startsWith(string prefix) {
//        TrieTreeNode *p = root;
//        for (int i = 0; i < prefix.length(); ++i)
//        {
//            int u = prefix[i] - 'a';
//            if (p->children[u] == nullptr)
//            {
//                return false;
//            }
//            p = p->children[u];
//        }
//        return true;
//    }
//};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

int main(int argc, const char * argv[]) {
    // insert code here...
    Trie *tire = new Trie();
    tire->insert("app");
    tire->insert("apn");
    tire->insert("apple");
    tire->search("apple");
    return 0;
}
