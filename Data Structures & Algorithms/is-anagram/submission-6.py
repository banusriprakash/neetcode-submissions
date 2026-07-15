class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left=0
        for right in range(len(s)-1,-1,-1):
            if s[left]!=s[right]:
                return False
            left+=1

        return True