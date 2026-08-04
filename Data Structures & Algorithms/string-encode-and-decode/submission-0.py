class Solution:

    def encode(self, strs: List[str]) -> str:
        eL = ""
        for s in strs:
            eL += str(len(s)) + "#" + s
        return eL

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        n = ""
        while i < len(s):
            if s[i] != "#":
                n+=s[i]
                i +=1
            else:
                w = ""
                for l in range(i+1, i+1+(int(n))):
                    i = l
                    w += s[l]
                res.append(w)
                n = ""
                i+=1
        return res
            
