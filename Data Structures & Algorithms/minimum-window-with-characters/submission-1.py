class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""

        countT , window = {} , {}
        res , resLen = "" , float("infinity")

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have , need = 0 , len(countT)
        l_ptr = 0
        for r_ptr in range(len(s)):
            c = s[r_ptr]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r_ptr - l_ptr + 1) < resLen:
                    resLen = r_ptr - l_ptr + 1
                    res = s[l_ptr : r_ptr+1]

                window[s[l_ptr]] -= 1
                if s[l_ptr] in countT and window[s[l_ptr]] < countT[s[l_ptr]]:
                    have -= 1
                l_ptr += 1
        return res