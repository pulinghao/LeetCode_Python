#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/11 11:22 下午
 @Author   :pulinghao@baidu.com
 @File     :130. 被围绕的区域.py 
 @Description :
"""


class Solution(object):
    def __init__(self):
        self.dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        # 1.先找出边上的O


        for i in range(4):
            if i == 0:
                # 第一行
                for j in range(len(board[0])):
                    if board[0][j] == 'O':
                        board[0][j] = 'Y'
                        for dir in self.dirs:
                            dir_x = dir[0]
                            dir_y = dir[1]
                            self.track(board, dir_x, j + dir_y)
                        pass

                pass
            if i == 1:
                # 第一列
                for j in range(len(board)):
                    if board[j][0] == 'O':
                        board[j][0] = 'Y'
                        for dir in self.dirs:
                            dir_x = dir[0]
                            dir_y = dir[1]
                            self.track(board, j + dir_x, dir_y)
                        pass
                pass
            if i == 2:
                # 最后一行
                for j in range(len(board[0])):
                    if board[-1][j] == 'O':
                        board[-1][j] = 'Y'
                        for dir in self.dirs:
                            dir_x = dir[0]
                            dir_y = dir[1]
                            self.track(board, len(board) - 1 + dir_x, j + dir_y)
                        pass
                pass
            if i == 3:
                # 最后一列
                for j in range(len(board)):
                    if board[j][-1] == 'O':
                        board[j][-1] = 'Y'
                        for dir in self.dirs:
                            dir_x = dir[0]
                            dir_y = dir[1]
                            self.track(board, j + dir_x, len(board[0]) - 1 + dir_y)
                pass

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'Y':
                    board[i][j] = 'O'


    def track(self, board, i, j):
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
            return

        if board[i][j] == 'O':
            board[i][j] = 'Y'
            for dir in self.dirs:
                dir_x = dir[0]
                dir_y = dir[1]
                self.track(board, i + dir_x, j + dir_y)
        else:
            return
        pass

if __name__ == '__main__':
    board = [
        ["X","O","X","X"],
        ["X","O","X","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]
    board =[["O","X","X","X","X","O","O","X","O","X","X","X","X","X","X","O","O","X","X","O"],["O","O","O","O","O","O","X","O","X","O","X","O","O","X","X","O","O","O","X","O"],["O","X","O","X","O","X","O","X","O","O","X","X","X","O","O","O","O","O","O","X"],["X","O","O","X","X","X","X","X","O","X","O","O","O","O","X","O","X","O","X","O"],["O","X","O","O","O","O","X","O","O","O","O","X","O","O","X","O","X","X","X","O"],["O","O","O","O","O","O","O","X","O","X","X","O","O","X","X","O","O","X","O","X"],["O","O","X","X","X","X","O","X","X","X","X","O","O","O","X","O","X","O","X","X"],["X","X","X","X","O","O","X","O","X","O","O","O","O","O","O","X","X","X","O","X"],["X","O","O","O","X","X","O","O","X","O","X","X","O","O","O","X","O","O","O","O"],["X","O","O","X","O","X","O","X","O","O","X","X","X","O","O","O","O","O","X","O"],["O","O","O","X","O","O","X","O","O","O","O","O","O","X","O","X","O","O","X","X"],["O","X","O","O","X","X","X","O","X","X","X","O","O","O","X","O","X","O","O","O"],["X","X","X","O","X","X","O","X","O","X","O","X","X","O","O","O","X","O","O","O"],["O","X","X","O","X","O","O","X","X","O","X","X","O","X","X","O","X","X","O","O"],["O","X","X","O","O","X","O","O","O","X","O","X","O","O","O","O","O","O","X","X"],["O","O","X","O","O","O","X","X","O","X","X","X","X","O","X","O","X","O","X","O"],["X","O","O","O","X","O","X","O","X","O","O","O","O","X","X","O","O","O","O","O"],["X","O","O","X","X","O","O","X","X","O","O","O","X","O","O","O","X","X","X","O"],["O","X","O","X","X","O","O","O","X","X","O","O","X","X","X","O","O","X","X","O"],["O","O","X","O","X","O","O","O","O","O","O","O","O","X","O","X","O","O","X","O"]]
    Solution().solve(board)
    print board