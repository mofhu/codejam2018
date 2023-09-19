# author: mofhu@github
# 100020. Minimum Array Length After Pair Removals

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
    # def minLengthAfterRemovals(self, nums):
        maxeq = 0
        i = 0
        while i < len(nums) -1:
            j = i+1
            while j < len(nums) and nums[j] == nums[i] :
                j += 1
            else:
                eq = j-i
                if eq > maxeq:
                    maxeq = eq
                i = j
        # print('maxeq', maxeq)
        if maxeq * 2 <= len(nums):
            # print(len(nums) % 2)
            return len(nums) % 2
        else:
            # print( maxeq - (len(nums) - maxeq))
            return maxeq - (len(nums) - maxeq)

a = Solution()
a.minLengthAfterRemovals([2, 3,3,3])
a.minLengthAfterRemovals([1, 2, 3,3,3])

