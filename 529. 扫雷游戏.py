#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/21 11:35 下午
 @Author   :pulinghao@baidu.com
 @File     :529. 扫雷游戏.py
 @Description :
"""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x = click[0]
        y = click[1]
        memo = {}  # 记忆化搜索

        if board[x][y] == 'M':
            board[x][y] = 'X'

        if board[x][y] == 'E':
            self.__dfs(board,x,y,memo)
            pass

        return board

    def __dfs(self, board, x, y, memo):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return

        key = str(x) + ',' + str(y)
        if key in memo.keys():
            return

        memo[key] = 1

        bombs = self.check(board, x, y)
        if bombs > 0:
            board[x][y] = str(bombs)
        else:
            # 周边没有雷
            board[x][y] = 'B'
            for dir in [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]:
                dir_x = dir[0]
                dir_y = dir[1]
                self.__dfs(board,x + dir_x,y + dir_y,memo)


    def check(self, board, x, y):
        # 检查周围有没有雷
        cnt = 0

        def ck(board, x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return False
            if board[x][y] == 'M':
                return True
            else:
                return False

        for dir in [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]:
            dir_x = dir[0]
            dir_y = dir[1]
            if ck(board, dir_x + x, dir_y + y):
                cnt += 1

        return cnt


if __name__ == '__main__':
    board = [['B', '1', 'E', '1', 'B'],['B', '1', 'M', '1', 'B'],['B', '1', '1', '1', 'B'],['B', 'B', 'B', 'B', 'B']]
    click = [1,2]
    print Solution().updateBoard(board,click)