# author: mofhu@github
# 6132. Make Array Zero by Subtracting Equal Amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        i = 0
        while nums[-1] > 0:
            while i < len(nums) and nums[i] == 0:
                i += 1
            t = nums[i]
            for j in range(i, len(nums)):
                nums[j] -= t
            ans += 1
        return ans

