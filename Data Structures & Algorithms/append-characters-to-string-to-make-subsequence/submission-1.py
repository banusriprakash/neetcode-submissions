class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not s:
            return 0

        p1=0

        for p2 in range(len(t)):
            if s[p1]==t[p2]:
                p1+=1

                if p1==len(s):
                    return len(s)-p1

        return len(t)-p1
       
        