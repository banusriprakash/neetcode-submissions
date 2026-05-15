class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}
        for i in range(0,len(s),1):
            mp[s[i]]=mp.get(s[i],0)+1

        for j in range(0,len(t),1):
            mp[t[j]]=mp.get(t[j],0)-1

        for val in mp.values():
            if val!=0:
                return False

        return True
        