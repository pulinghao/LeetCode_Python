#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/5 9:43 下午
 @Author   :pulinghao@baidu.com
 @File     :37. 解数独.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        char = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        def isValid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False

                if board[i][col] == num:
                    return False

                if board[(row / 3) * 3 + i / 3][(col / 3) * 3 + i % 3] == num:
                    return False
            return True

        # i,j 待填入的数字
        def backtrack(board, i, j):
            m = 9
            n = 9
            if j == n:
                # 从下一行开始
                return backtrack(board, i + 1, 0)

            if i == m:
                return True
            if board[i][j] != '.':
                # 原来位置上就有数字
                return backtrack(board, i, j + 1)

            for k in range(9):
                # 判断是否合法
                if not isValid(board,i,j,char[k]):
                    continue
                board[i][j] = char[k]
                if backtrack(board, i, j + 1):
                    return True
                board[i][j] = '.'

            return False


        backtrack(board,0,0)


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = leetcode_utils.stringToChar2dArray(line)

    ret = Solution().solveSudoku(board)

    out = leetcode_utils.char2dArrayToString(board)
    if ret is not None:
        print "Do not return anything, modify board in-place instead."
    else:
        print out
