class Solution:
    def firstUniqChar(self, s: str) -> int:

        frq=[0]*26
        
        for ch in s:
            frq[ord(ch)-ord('a')]+=1

        for i,ch in enumerate(s):
            print(f"index:{i} and Character:{ch}")
            if frq[ord(ch)-ord('a')]==1:
                return i

        return -1

        