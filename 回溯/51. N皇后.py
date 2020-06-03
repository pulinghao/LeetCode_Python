#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/2 10:30 下午
 @Author   :pulinghao@baidu.com
 @File     :51. N皇后.py 
 @Description :
"""
import copy

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # row 表示当前要放的行数(从第一行开始)，也可以理解为决策树的深度

        def backtrack(board, row):
            if row == len(board):
                board_copy = copy.deepcopy(board)
                res_board = []
                for row in board_copy:
                    newrow = ''.join(row)
                    res_board.append(newrow)
                res.append(res_board)
                return

            for col in range(n):
                if not isValid(board,row,col):
                    continue

                board[row][col] = 'Q'
                backtrack(board,row + 1)
                board[row][col] = '.'
            pass

        def isValid(board,row,col):
            # 假设这个位置有皇后，攻击同一行、同一列、左上左下右上右下四个方向的任意单位。
            # 同一列（因为这一行就是要放Q的行，所以肯定满足要求，对同一行不需要验证）
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False

            # 检查右上方
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            # 检查左上方
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            return True
        res = []

        # 初始化空棋盘
        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(board,0)
        return res

if __name__ == '__main__':
    print Solution().solveNQueens(n = 4)