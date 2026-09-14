class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0 
        count = 0
        mcount = 0
        map = {}
        for r in range(len(fruits)):
            map[fruits[r]] = map.get(fruits[r], 0) + 1
            count += 1
            while len(map) > 2:
                f = fruits[l]
                map[f] -= 1
                l += 1
                count -= 1
                if not map[f]:
                    map.pop(f)
            mcount = max(mcount, count)
        return mcount
            
            
