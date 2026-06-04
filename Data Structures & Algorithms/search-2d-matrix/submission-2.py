class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l_row = 0
        r_row = len(matrix) - 1

        row_select = -1

        while l_row <= r_row:
            mid = l_row + (r_row - l_row) // 2

            if matrix[mid][-1] < target:
                l_row = mid + 1
                
            elif matrix[mid][0] > target:
                r_row = mid - 1

            else:
                row_select = mid
                break

        if row_select == -1:
            return False

        l_col = 0
        r_col = len(matrix[0]) - 1
        
        while l_col <= r_col:

            mid = l_col + (r_col - l_col) // 2

            if matrix[row_select][mid] < target:
                l_col = mid + 1
                
            elif matrix[row_select][mid] > target:
                r_col = mid - 1

            else:
                return True

        return False