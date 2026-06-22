from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[c][r] == ".":
                    continue
                
                if board[c][r] in row[r] or board[c][r] in column[c] or board[c][r] in square[(c//3, r//3)]:
                    return False
                
                column[c].add(board[c][r])
                row[r].add(board[c][r])
                square[(c//3, r//3)].add(board[c][r])
        
        return True