class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t): return False
        mp={}

        for i in s:
            mp[i]=mp.get(i,0)+1
        
        for j in t:
            if j in mp:
                mp[j]=mp.get(j,0)-1

        print(mp)
        for val in mp.values():
            if val>0:
                return False

        return True

                
        