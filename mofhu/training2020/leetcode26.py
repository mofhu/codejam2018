class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        t = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > t:
                nums[j] = nums[i]
                j += 1
                t = nums[j]
        return j

