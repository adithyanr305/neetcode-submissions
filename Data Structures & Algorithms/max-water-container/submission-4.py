class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        output = 0
        l,r = 0, len(heights) - 1

        while r > l:
            width = r - l
            height = min(heights[r], heights[l])
            area = height*width 
            output = max(output, area) 

            # move pointers
            if heights[r] < heights[l]:
                prev = heights[r]
                while heights[r] <= prev and r > l:
                    r -= 1
            else:
                prev = heights[l]
                while heights[l] <= prev and r > l:
                    l += 1
        return output


