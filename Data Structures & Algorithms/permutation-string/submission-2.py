class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sd1 = {}
        for ch in s1:
            sd1[ch] = 1 + sd1.get(ch,0)
        l = 0
        r = len(s1)
        while r <= len(s2):
            sd2 = {}
            window = s2[l:r]
            if s2[l] in s1 and s2[r-1] in s1: 
                for ch in window:
                    sd2[ch] = 1 + sd2.get(ch,0)    
                if sd1 == sd2:
                    return True
            l += 1
            r += 1
        return False
            