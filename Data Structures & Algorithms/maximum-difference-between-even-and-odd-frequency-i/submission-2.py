class Solution:
    def maxDifference(self, s: str) -> int:
        
        if not s:
            return 0

        mp={}

        for ch in s:
            mp[ch]=mp.get(ch,0)+1

        s_m=set(sorted(mp.values(),key=lambda item:item,reverse=True))
        ls=list(s_m)
        print(ls)

        

        return ls[len(ls)-1]-ls[len(ls)-2] if ls[len(ls)-1]>ls[len(ls)-2] else ls[len(ls)-2]-ls[len(ls)-1]