class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        st = []
        for i in range(len(s)):
            if s[i] in closeToOpen:
                if st and st[-1] == closeToOpen[s[i]]:
                    st.pop()
                else:
                    return False
            else:
                st.append(s[i])
        
        if len(st) == 0:
            return True
        return False

