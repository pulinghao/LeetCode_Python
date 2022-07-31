//
//  main.cpp
//  剑指 Offer 12. 矩阵中的路径
//
//  Created by pulinghao on 2022/6/28.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int h = board.size();
        int w = board[0].size();
        vector<vector<int>> visited(h, vector<int>(w));
        bool res = false;
        res = backtrack(board,visited,word,0,0,0);
        return res;
    }


/*
* board 原矩阵
* visited 已访问过

*/
    bool backtrack(vector<vector<char>> &board, vector<vector<int>> &visited, string word, int x , int y , int k){
        // 终止条件
        if (x < 0 || y < 0 || x >= board.size() || y>= board[0].size())
        {
            return false;
        }
        
        if(board[x][y] != word[k]){
            return false;
        }

        if (visited[x][y])
        {
            return false;
        }

        if (k == word.size() - 1)
        {
            return true;
        }


        bool result = false;
        // 选择
        // 这个位置的字符正确
        visited[x][y] = 1;
        vector<vector<int>> dirs = {{1,0},{0,1},{-1,0},{0,-1}};
        for (int i = 0; i < dirs.size(); ++i)
        {
            vector<int> dir = dirs[i];
            int dir_x = dir[0];
            int dir_y = dir[1];
            bool flag = backtrack(board, visited, word, x + dir_x,y + dir_y, k + 1);
            if (flag)
            {
                result = true;
            }
        }

        // 回退
        visited[x][y] = 0;
        return result;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string board = "[[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]]";
//    vector<vector<char>> input = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    vector<vector<char>> input = {{'a','b'}};
    std::cout << Solution().exist(input, "ba");
    return 0;
}
