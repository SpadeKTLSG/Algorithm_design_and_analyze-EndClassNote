# -*- coding: utf-8 -*-
# 应该算是最标准的解法了

def solveNQueens(n):
    def print_board(board):  # 打印棋盘
        for i in board:
            for j in i:
                print(j)
            print('\n')

    def isValid(row, col, board):  # 限制条件
        # 注：左斜对角线上，同一条斜线上的每个位置满足行下标与列下标之差相等; 右斜对角线上，同一条斜线上的每个位置满足行下标与列下标之和相等
        for i in range(row):
            for j in range(n):
                if board[i][j] == 'Q' and (j == col or i + j == row + col or i - j == row - col):
                    return False
        return True

    def backtrack(board, row):  # 回溯算法
        if row >= n:
            cur_res = [''.join(row) for row in board]
            res.append(cur_res)
            return
        for i in range(n):
            if isValid(row, i, board):
                board[row][i] = 'Q'
                backtrack(board, row + 1)
                board[row][i] = '.'

    res = []
    board = [['.'] * n for _ in range(n)]
    backtrack(board, 0)
    print_board(res)


if __name__ == '__main__':
    solveNQueens(4)
