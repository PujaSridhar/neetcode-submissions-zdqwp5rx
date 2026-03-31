class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0
        while left < right:
            width = right - left
            height = min(heights[left],heights[right])
            current_area = height * width
            water = max(water,current_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return water
        