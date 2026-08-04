class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_map = dict()
        for i,v in enumerate(nums):
            d = target - v
            if d in d_map:
                return [d_map[d],i]
            d_map[v] = i       