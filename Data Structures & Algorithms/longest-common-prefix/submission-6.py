class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        f=strs[0]
        j=0
        for i in range(1,len(strs)):
            if f[0:i] not in strs[i]:
                break

            j+=1

        return f[0:j] if j>0 else ""
