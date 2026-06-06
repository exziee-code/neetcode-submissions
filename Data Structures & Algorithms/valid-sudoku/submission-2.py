from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        for r in range(9): 
            for c in range(9):
                itm = board[r][c]
                if itm == ".":
                    continue
                
                if (itm in row[r] or itm in column[c] or itm in square[(r//3,c//3)]):
                    return False
                
                row[r].add(itm)
                column[c].add(itm)
                square[(r//3,c//3)].add(itm)
        
        return True