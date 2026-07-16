class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        if not s:
            return len(t)

        p1=0

        for p2 in range(len(t)):

            if s[p1]==t[p2]:
                p1+=1

                if p1==len(s):
                    return 0

        return abs(len(t)-p1)