class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'[':']', '{':'}', '(':')'}
        st = []
        for ch in s:
            if ch in pairs.keys():
                st.append(ch)
            else:
                if st and pairs[st[-1]] is ch:
                    st.pop()
                else:
                    return False
        return not st