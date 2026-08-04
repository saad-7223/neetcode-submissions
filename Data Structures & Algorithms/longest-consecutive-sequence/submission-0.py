class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longg = 0
        nset = set(nums)
        for n in nums:
            if n-1 not in nset:
                count = 0
                while (count+n) in nset:
                    count +=1
                longg = max(longg,count)
        return longg