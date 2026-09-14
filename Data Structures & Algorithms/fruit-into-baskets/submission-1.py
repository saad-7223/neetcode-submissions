class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        seen = set()
        count = 0
        mcount = 0
        while len(fruits) > r:
            if fruits[r] not in seen:
                seen.add(fruits[r])
            
            if len(seen) <= 2:
                count += 1
                r += 1
                if count > mcount:
                    mcount = count
                continue
            else:
                count = 0
                seen = set()
                l += 1
                r = l

        return mcount
            
            
