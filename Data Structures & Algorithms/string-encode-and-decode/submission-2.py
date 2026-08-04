class Solution:

    def encode(self, strs: List[str]) -> str:
        eL = ""
        for s in strs:
            eL += str(len(s)) + "#" + s
        return eL

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            k = i
            while s[k] != "#":
                k +=1
            l = int(s[i:k])
            i = k+1
            j = i+l
            res.append(s[i:j])
            i=j
        return res
            
