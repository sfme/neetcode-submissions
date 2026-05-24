class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        squares_set = [set() for _ in range(9)]
        
        for row_idx in range(9):
            for col_idx in range(9):
                val = board[row_idx][col_idx]
                
                if val == '.':
                    continue
                
                # index of the 3x3 square
                square_idx = (row_idx // 3) * 3 + (col_idx // 3)
                
                # check duplicates in row, col, or square sets
                if val in rows_set[row_idx] or val in cols_set[col_idx] or val in squares_set[square_idx]:
                    return False
                    
                # no duplicates, add value to sets
                rows_set[row_idx].add(val)
                cols_set[col_idx].add(val)
                squares_set[square_idx].add(val)
                
        return True



        