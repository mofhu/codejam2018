class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        end = len(height) - 1
        maxarea = (end - front) * min(height[front], height[end])
        while (end - front) > 1:
            if height[front] <= height[end]:
                while height[front+1] <= height[front] and front < end:
                    front += 1
                front += 1
            elif height[front] > height[end]:
                while height[end-1] <= height[end] and front < end:
                    end -= 1
                end -= 1
            # print(front, end)
            t = (end - front) * min(height[front], height[end])
            if t > maxarea:
                maxarea = t

        return maxarea
