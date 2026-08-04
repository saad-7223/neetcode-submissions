class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lb = 1
        ub = max(piles)
        k = ub
        while lb <= ub:
            m = (lb+ub)//2
            s = 0
            for val in piles:
                s += math.ceil(val/m)
            if s <= h:
                k = m
                ub = m-1
            if s > h:
                lb = m+1
        return k 
                       