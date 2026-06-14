class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        len_rows, len_cols = len(grid), len(grid[0])
        q = deque()
        
        fresh_oranges = 0
        minutes = 0

        # find all rotten oranges and count fresh ones
        for i in range(len_rows):
            for j in range(len_cols):
                if grid[i][j] == 2: # rotten
                    q.append((i, j))
                elif grid[i][j] == 1: # fresh
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        while q and fresh_oranges > 0:
            minutes += 1
            
            # process only the oranges that are currently rotten this batch
            for _ in range(len(q)):
                cur_i, cur_j = q.popleft()
                
                for i_dir, j_dir in dirs:
                    next_i = cur_i + i_dir
                    next_j = cur_j + j_dir
                    
                    # if neighbor fresh orange, then becomes rotten
                    if (0 <= next_i < len_rows 
                        and 0 <= next_j < len_cols 
                        and grid[next_i][next_j] == 1):
                        
                        grid[next_i][next_j] = 2 # mark rotten
                        fresh_oranges -= 1
                        q.append((next_i, next_j))
                        
        return minutes if fresh_oranges == 0 else -1


