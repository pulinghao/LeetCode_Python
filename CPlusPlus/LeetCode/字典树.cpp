struct TreeNode
{
    bool end;
    std::vector<TreeNode> children(26);
};

class Trie {
private:
    TreeNode *root;
public:
    Trie() {
        root = new TreeNode();
    }
    
    void insert(string word) {
        TreeNode *p = root;
        for (int i = 0; i < word.length(); ++i)
        {
            int u = word[i] - 'a';
            if (p->children[u] == nullptr)
            {
                p->children[u] = new TreeNode(u);
            }
            p = p->children[u];
        }
        p->end = true;
    }
    
    bool search(string word) {

    }
    
    bool startsWith(string prefix) {

    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */