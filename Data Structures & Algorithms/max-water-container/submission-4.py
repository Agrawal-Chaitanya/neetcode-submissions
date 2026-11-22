class Solution:
    def area(self, heights, left, right):
        return min(heights[left], heights[right])*(right-left)

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:
            max_area = max(self.area(heights, left, right), max_area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return max_area
        