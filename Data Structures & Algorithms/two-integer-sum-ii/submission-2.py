class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dih = {}
        for i,v in enumerate(numbers):
            diff = target - v
            if diff not in dih:
                dih[v] = i+1
                continue
            return [dih[diff],i+1]