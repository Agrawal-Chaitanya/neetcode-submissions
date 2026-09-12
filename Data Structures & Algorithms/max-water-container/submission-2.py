class Solution:
    def area(self, left, right, heights):
        return (right-left)*min(heights[left], heights[right])

    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_arr = 0
        while left< right:
            arr = self.area(left, right, heights)
            max_arr = max(max_arr, arr)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return max_arr

        