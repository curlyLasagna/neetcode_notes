from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        right: int = len(heights) - 1
        left: int = 0
        while left < right:
            area = (right - left) * min(heights[right], heights[left])
            maxArea = max(maxArea, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea


Solution().maxArea([1, 7, 2, 5, 4, 7, 3, 6])
