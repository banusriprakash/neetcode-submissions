class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        mp={}

        for ch1 in s:
            mp[ch1]=mp.get(ch1,0)+1

        for ch2 in t:
            mp[ch2]=mp.get(ch2,0)-1

        for val in mp.values():
            if val>0:
                return False

        return True