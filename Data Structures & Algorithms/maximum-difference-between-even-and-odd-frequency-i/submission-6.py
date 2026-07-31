class Solution:
    def maxDifference(self, s: str) -> int:
        
        if not s:
            return 0

        frq=[0]*26

        for ch in s:
            frq[ord(ch)-ord('a')]+=1

        max_odd=-float("inf")
        max_ev=-float("inf")

        for i in range(len(frq)):
            if frq[i]%2==1:
                max_odd=max(frq[i],max_odd)
            else:
                max_ev=max(frq[i],max_ev)
            
        return max_odd-max_ev
