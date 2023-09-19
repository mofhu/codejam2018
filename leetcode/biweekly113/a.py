# author: mofhu@github
# 8039. Minimum Right Shifts to Sort the Array

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n == 1:
            return 0
        else:
            while ans < n:
                for i in range(n-1):
                    if nums[i] > nums[i+1]:
                        break
                else:
                    return ans
                nums = [nums[-1]] + nums[:-1]
                ans += 1
            else:
                return -1


