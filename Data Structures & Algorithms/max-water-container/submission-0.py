class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumArea = 0
        l = 0
        r = len(heights)-1
        while l != r:
            w = abs(l-r)
            h = min(heights[l],heights[r])
            a = w*h
            if a > maximumArea:
                maximumArea = a
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maximumArea