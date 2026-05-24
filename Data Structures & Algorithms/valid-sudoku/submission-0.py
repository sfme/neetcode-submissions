class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        squares_set = [set() for _ in range(9)]

        # check rows
        for idx, row in enumerate(board):
            for elem in row:
                if elem == '.': # Skip empty cells
                    continue

                if elem in rows_set[idx]:
                    return False
                else:
                    rows_set[idx].add(elem)

        # check cols
        for idx, col in enumerate(zip(*board)):
            for elem in col:
                if elem == '.': # Skip empty cells
                    continue

                if elem in cols_set[idx]:
                    return False
                else:
                    cols_set[idx].add(elem)

        # check squares
        for ii in range(9): # number of boxes
            _set_square = squares_set[ii]

            for jj in range(9): # cell inside the box       
                row = (ii // 3) * 3 + (jj // 3)
                col = (ii % 3) * 3 + (jj % 3)
                cell_value = board[row][col]

                if cell_value == '.': # Skip empty cells
                    continue

                if cell_value in _set_square:
                    return False
                else:
                    _set_square.add(cell_value)

        return True



        