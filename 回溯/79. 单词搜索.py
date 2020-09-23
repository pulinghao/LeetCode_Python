#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/13 7:41 下午
 @Author  :pulinghao@baidu.com
 @File     :79. 单词搜索.py
 @Description :
"""


class Solution(object):
    def __init__(self):
        self.res = False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        N = len(board)
        M = len(board[0])
        res = False

        if M * N < len(word):
            return False

        def dfs(board, word, wordidx, path, visited, i, j, res):
            if i < 0 or j < 0 or i >= N or j >= M:
                return

            if wordidx >= len(word):
                return

            b = board[i][j]
            w = word[wordidx]
            if word[wordidx] == board[i][j]:
                path.append(board[i][j])
                if len(path) == len(word):
                    self.res = True
                    return
                for dir in dirs:
                    x = dir[0] + i
                    y = dir[1] + j
                    if x < 0 or y < 0 or x >= N or y >= M:
                        continue

                    if visited[x][y] == 1:
                        continue

                    visited[x][y] = 1
                    dfs(board, word, wordidx + 1, path, visited, x, y, res)
                    visited[x][y] = 0
                path.pop(-1)
            return

        path = []
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                path = []
                if board[i][j] == word[0]:
                    path.append(word[0])
                    if len(path) == len(word):
                        return True
                    visited[i][j] = 1
                    for dir in dirs:
                        x = dir[0] + i
                        y = dir[1] + j
                        if x < 0 or y < 0 or x >= N or y >= M:
                            continue
                        if visited[x][y] == 1:
                            continue
                        visited[x][y] = 1
                        dfs(board, word, 1, path, visited, x, y, res)
                        visited[x][y] = 0
                        if self.res:
                            return self.res
                    visited[i][j] = 0
                    path.pop(-1)

        return self.res


if __name__ == '__main__':
    board = [["a","a","b","b"],["a","a","b","b"]]
    word = "baa"
    print Solution().exist(board, word)
