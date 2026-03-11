from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        cnt = 0
        row = 0
        col = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row = i
                    col = j
                    break
        for i in range(1, row + 1):
            curr_row = row - i
            if board[curr_row][col] == 'B':
                break
            elif board[curr_row][col] == 'p':
                cnt += 1
                break
        for curr_row in range(row + 1, 8):
            if board[curr_row][col] == 'B':
                break
            elif board[curr_row][col] == 'p':
                cnt += 1
                break
        for i in range(1, col + 1):
            curr_col = col - i
            if board[row][curr_col] == 'B':
                break
            elif board[row][curr_col] == 'p':
                cnt += 1
                break
        for curr_col in range(col + 1, 8):
            if board[row][curr_col] == 'B':
                break
            elif board[row][curr_col] == 'p':
                cnt += 1
                break
        return cnt