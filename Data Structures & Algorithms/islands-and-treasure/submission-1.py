
from collections import deque

class Solution:
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        len_rows, len_cols = len(grid), len(grid[0])
        q = deque() # queue

        for i in range(len_rows):
            for j in range(len_cols):
                if grid[i][j] == 0:
                    q.append((i,j))


        while q:
            cur_i, cur_j = q.popleft()

            for i_dir, j_dir in dirs:

                next_i = cur_i + i_dir
                next_j = cur_j + j_dir

                if (0 <= next_i < len_rows 
                    and 0 <= next_j < len_cols 
                    and grid[next_i][next_j] == 2147483647):

                    grid[next_i][next_j] = grid[cur_i][cur_j] + 1

                    q.append((next_i, next_j))
        
        

            


