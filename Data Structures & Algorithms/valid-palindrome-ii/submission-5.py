class Solution:
    def validPalindrome(self, s: str) -> bool:

        if not s:
            return True

        i,j=0,len(s)-1
        cnt=1
        while i<j:
            if s[i]!=s[j]:
                skip_left=s[i+1:j+1]
                print(skip_left)
                skip_right=s[i:j]
                print(skip_right)
                return skip_left==skip_left[::-1] or skip_right==skip_right[::-1]
            i+=1
            j-=1

        return True
        