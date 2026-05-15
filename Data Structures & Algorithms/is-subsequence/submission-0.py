class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       return Solution.rec(s,t,0,0)

    @staticmethod    
    def rec(s:str,t:str,i:int,j:int)->bool:
        if i==len(s): return True
        if j==len(t): return False

        if(s[i]==t[j]):
            return Solution.rec(s,t,i+1,j+1)

        return Solution.rec(s,t,i,j+1)
        
            
        