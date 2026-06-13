
def valid_move(ii: int , jj: int, len_rows: int, len_cols: int) -> bool:

    if ii < 0 or ii >= len_rows:
        return False

    if jj < 0 or jj >= len_cols:
        return False
    
    return True

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        len_rows = len(grid)
        len_cols = len(grid[0])

        visited = set()
        max_area = 0

        for i in range(len_rows):
            for j in range(len_cols):

                if (i,j) not in visited and grid[i][j]:
                    stack = [(i,j)]
                    cur_area = 0

                    while stack:
                        cur_i, cur_j = stack.pop()

                        if (cur_i, cur_j) not in visited:
                            visited.add((cur_i,cur_j))
                            cur_area += 1

                            for di, dj in dirs:
                                next_i = cur_i + di
                                next_j = cur_j + dj

                                if (valid_move(next_i, next_j, len_rows, len_cols)
                                    and grid[next_i][next_j]
                                    and (next_i, next_j) not in visited):

                                    stack.append((next_i, next_j))

                    max_area = max(max_area, cur_area)

        return max_area