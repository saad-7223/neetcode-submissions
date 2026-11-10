class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSm = 0
        prefixsm = {0:1}

        for n in nums:
            curSm += n
            diff = curSm - k

            res += prefixsm.get(diff,0)
            prefixsm[curSm] = 1 + prefixsm.get(curSm,0)

        return res