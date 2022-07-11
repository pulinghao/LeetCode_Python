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

class Trie {
private:
    TrieTreeNode *root;
public:
    Trie() {
        root = new TrieTreeNode();
    }
    
    void insert(string word) {
        TrieTreeNode *p = root;
        for (int i = 0; i < word.length(); ++i)
        {
            int u = word[i] - 'a';
            if (p->children[u] == nullptr)
            {
                p->children[u] = new TrieTreeNode();
            }
            p = p->children[u];
        }
        p->end = true;
    }
    
    bool search(string word) {
        TrieTreeNode *p = root;
        for (int i = 0; i < word.length(); ++i)
        {
            int u = word[i] - 'a';
            if (p->children[u] == nullptr)
            {
                return false;
            }
            p = p->children[u];
        }
        return p->end;
    }
    
    bool startsWith(string prefix) {
        TrieTreeNode *p = root;
        for (int i = 0; i < prefix.length(); ++i)
        {
            int u = prefix[i] - 'a';
            if (p->children[u] == nullptr)
            {
                return false;
            }
            p = p->children[u];
        }
        return true;
    }
};

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
    tire->insert("apple");
    tire->search("apple");
    return 0;
}
