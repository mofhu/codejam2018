# author: mofhu@github
# 6133. Maximum Number of Groups Entering a Competition

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        ans = 1
        t0 = ans
        i = 1 + 1
        t = len(grades)
        while t0 + i <= t:
            t0 += i
            i += 1
            ans += 1
        return ans



