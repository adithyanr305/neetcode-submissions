class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxi = 0
        while l < r:
            vol = min(heights[l],heights[r])*(r-l)
            maxi = max(maxi,vol)
            if heights[l] < heights[r]:
                prev = heights[l]
                while heights[l] <= prev and l < r:
                    l += 1
            else:
                prev = heights[r]
                while heights[r] <= prev and l < r:
                    r -= 1
        return maxi