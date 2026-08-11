class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
        mp={}

        for ch in s:
            mp[ch]=mp.get(ch,0)+1

        cnt=1
        print(mp)
        for v in mp.values():
            if v%2==1:
                cnt-=1
                
        return True if cnt>=0 else False