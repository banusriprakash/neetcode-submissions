class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        f = strs[0]
        j = 0
        
        while j < len(f):
            for i in range(1, len(strs)):
                val = strs[i]
                
                # Check if j exceeds the length of the current string 
                # OR if the characters mismatch at index j
                if j == len(val) or f[j] != val[j]:
                    return f[0:j] # Immediately exit and return the prefix found so far
            
            j += 1
            
        return f[0:j]