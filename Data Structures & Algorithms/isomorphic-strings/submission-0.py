class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1={}
        mp2={}

        for ch1 in s:
            mp1[ch1]=mp1.get(ch1,0)+1

        for ch2 in t:
            mp2[ch2]=mp2.get(ch2,0)+1

        ls1=list(mp1.values())
        ls1.sort()
        print(ls1)
        ls2=list(mp2.values())
        ls2.sort()
        print(ls2)
        if len(ls1)!=len(ls2):
            return False
        
        for i in range(len(ls1)):
            if ls1[i]!=ls2[i]:
                return False
        
        return True