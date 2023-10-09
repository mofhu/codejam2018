# author: mofhu@github
# 100085. Minimum Processing Time

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        ans = 0
        for i in range(len(processorTime)):
            if processorTime[i] + tasks[4*i+3] > ans:
                ans = processorTime[i] + tasks[4*i+3]
        return ans
