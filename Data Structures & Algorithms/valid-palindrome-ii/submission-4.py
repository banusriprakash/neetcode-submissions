class Solution:
    def validPalindrome(self, s: str) -> bool:

        if not s:
            return True

        i,j=0,len(s)-1
        cnt=1
        while i<j:
            if s[i]!=s[j]:
                if cnt==0:
                    return False
                cnt-=1
            i+=1
            j-=1

        return True
        