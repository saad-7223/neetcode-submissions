class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [1,0]:
            return len(s)
        
        setWords = set()
        newS = ""
        for i in s:
            if i in newS:
                if newS not in setWords:
                    setWords.add(newS)
                newS = newS[newS.index(i) + 1:]    
            newS += i
        setWords.add(newS)
        return len(max(setWords,key=len))
