# author: mofhu@github
# 6129. Number of Zero-Filled Subarrays

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append(1)
        ans = 0
        z0 = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0:
                if flag == False:
                    flag = True
                    z0 = i
                else:
                    pass
            else:
                if flag == True:
                    flag = False
                    ans += (i-z0+1)*(i-z0)//2
        return ans



