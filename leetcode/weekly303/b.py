# author: mofhu@github
# 6125. Equal Row and Column Pairs

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        for i in range(len(grid)):
            cols.append([grid[j][i] for j in range(len(grid))])
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                for k in range(len(grid)):
                    if grid[i][k] != cols[j][k]:
                        break
                else:
                    ans += 1
        return ans



