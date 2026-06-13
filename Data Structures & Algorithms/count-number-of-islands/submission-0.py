
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        number_of_clusters = 0

        n_rows = len(grid)
        n_cols = len(grid[0])

        visited = set()

        for ii in range(n_rows):
            for jj in range(n_cols):

                if grid[ii][jj] == "1" and (ii,jj) not in visited:
                    number_of_clusters += 1
                    stack = [(ii, jj)]

                    while stack:
                        
                        cur_i, cur_j = stack.pop()
                        if (cur_i, cur_j) not in visited:

                            visited.add((cur_i, cur_j))
                            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                            for di, dj in directions:
                                next_i = cur_i + di
                                next_j = cur_j + dj

                                if (0 <= next_i < n_rows and 
                                    0 <= next_j < n_cols and 
                                    grid[next_i][next_j] == "1" and 
                                    (next_i, next_j) not in visited):
                                    
                                    stack.append((next_i, next_j))

        return number_of_clusters



                



                




                



        