class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        if len(tokens) <= 1:
            return int(tokens[0])
        for i in tokens:
            if i not in ['+','-','*','/']:
                st.append(i)
            else:
                x = int(st.pop())
                y = int(st.pop())
                if i == "+":
                    s = y+x
                if i == "-":
                    s = y-x
                if i == "*":
                    s = y*x
                if i=="/":
                    s = int(y/x)
                st.append(s)
        return st[0]