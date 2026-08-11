class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = 1000000000
        l = 0
        r = 0
        while (r <= len(nums)):
            if l == r:
                if nums[l] >= target:
                    minLen = 1
                    r += 1
                    break 
                       
            winSum = sum(nums[l:r+1])
            if winSum < target:
                r += 1
            
            elif winSum >= target:
                size = len(nums[l:r+1])
                l += 1
                if size < minLen:
                    minLen = size

        if minLen == 1000000000:
            return 0    
        return minLen
