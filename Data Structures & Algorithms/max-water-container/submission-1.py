class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = min(heights[l], heights[r]) * (len(heights) - 1)
        while l < r:
            while (heights[l] > heights[r]) and l < r:
                if (heights[r-1] > heights[r]) and not r-1 == l:
                    maxArea = max(maxArea, min(heights[r-1], heights[l]) * (r - l - 1))
                r -= 1
            while heights[l] < heights[r] and l < r:
                if (heights[l+1] > heights[l]) and not l+1 == r:
                    maxArea = max(maxArea, min(heights[l+1], heights[r]) * (r - l - 1))
                l += 1
            if (heights[l] == heights[r]):
                maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))
                l += 1
        return maxArea          