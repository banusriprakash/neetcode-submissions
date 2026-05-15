class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        arr=[0]*128

        for i in range(len(s)):
            arr[ord(s[i])]+=1

        for i in range(len(t)):
            arr[ord(t[i])]-=1

        for i in arr:
            if i!=0:
                return False

        return True