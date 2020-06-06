#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/5 10:09 下午
 @Author   :pulinghao@baidu.com
 @File     :36. 有效的数独.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    if i != col:
                        return False

                if board[i][col] == num:
                    if i != row:
                        return False

                if board[(row / 3) * 3 + i / 3][(col / 3) * 3 + i % 3] == num:
                    if (row / 3) * 3 + i / 3 != row and (col / 3) * 3 + i % 3 != col:
                        return False
            return True
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                if not isValid(board,i,j,board[i][j]):
                    return False
                    break

        return True

if __name__ == '__main__':
    board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]
]


    ret = Solution().isValidSudoku(board)

    print ret