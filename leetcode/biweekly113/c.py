# author: mofhu@github
# 6988. Count Pairs of Points With Distance k

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        # key: k<=100
        ans = 0
        n = len(coordinates)
        coordinates.sort()
        dof = set()  # overflow
        ans = 0
        for i in range(n):
            j = i+1
            while j < n:
                xi, yi, xj, yj = coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]
                if (xi, xj) in dof or (yi, yj) in dof:
                    pass
                else:
                    x = xi ^ xj
                    y = yi ^ yj
                    if x > k:
                        dof.add((xi,xj))
                    if y > k:
                        dof.add((yi,yj))
                    if x + y == k:
                        ans += 1
                j += 1

        return ans

