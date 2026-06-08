from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current == ".":
                    continue
                
                if (current in row[r] or current in column[c] or current in square[(r//3,c//3)]):
                    return False
                
                row[r].add(current)
                column[c].add(current)
                square[((r//3,c//3))].add(current)
        return True