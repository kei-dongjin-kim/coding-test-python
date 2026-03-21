from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        sq = [['', '', ''], ['', '', ''], ['', '', '']]
        for i, [r, c] in enumerate(moves):
            curr = 'A' if i % 2 == 0 else 'B'
            sq[r][c] = curr
            result: bool = self.judge(sq, r, c)
            if result:
                return curr
        if len(moves) < 9:
            return 'Pending'
        return 'Draw'
    
    def judge(self, sq: List[List[int]], r: int, c: int) -> bool:
        return (
            (sq[r][c] == sq[0][0] and sq[0][0] == sq[0][1] and sq[0][1] == sq[0][2]) or
            (sq[r][c] == sq[1][0] and sq[1][0] == sq[1][1] and sq[1][1] == sq[1][2]) or
            (sq[r][c] == sq[2][0] and sq[2][0] == sq[2][1] and sq[2][1] == sq[2][2]) or
            (sq[r][c] == sq[0][0] and sq[0][0] == sq[1][0] and sq[1][0] == sq[2][0]) or
            (sq[r][c] == sq[0][1] and sq[0][1] == sq[1][1] and sq[1][1] == sq[2][1]) or
            (sq[r][c] == sq[0][2] and sq[0][2] == sq[1][2] and sq[1][2] == sq[2][2]) or
            (sq[r][c] == sq[0][0] and sq[0][0] == sq[1][1] and sq[1][1] == sq[2][2]) or
            (sq[r][c] == sq[0][2] and sq[0][2] == sq[1][1] and sq[1][1] == sq[2][0])
        )
