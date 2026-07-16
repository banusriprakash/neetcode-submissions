class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        if not s:
            return len(t)

        p_s=0
        p_t=0

        while p_s<len(s) and p_t<len(t):
            if s[p_s]==t[p_t]:
                p_t+=1
            p_s+=1

        return len(t)-p_t