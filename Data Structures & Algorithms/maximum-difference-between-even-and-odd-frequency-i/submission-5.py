class Solution:
    def maxDifference(self, s: str) -> int:
        
        if not s:
            return 0

        mp={}

        for ch in s:
            mp[ch]=mp.get(ch,0)+1

        s_m=set(sorted(mp.values(),key=lambda item:item,reverse=True))
        ev=[v for v in s_m if v%2==0]
        od=[v for v in s_m if v%2==1]
        print(od)
        print(ev)

        

        return od[len(od)-1]-ev[len(ev)-1] if od[len(od)-1]>ev[len(ev)-1] else ev[len(ev)-1]-od[len(od)-1]
