class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        maxl , maxR = height[l], height[r]
        counter = 0
        while (l < r):
            if maxl < maxR:
                l += 1
                maxl = max(maxl, height[l])
                counter += maxl - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                counter += maxR - height[r]
        
        return counter