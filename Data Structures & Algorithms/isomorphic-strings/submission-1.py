class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        mp_s_t={}
        mp_t_s={}

        for i,j in zip(s,t):

            if i in mp_s_t:
                if mp_s_t[i]!=j:
                    return False

            if j in mp_t_s:
                if mp_t_s[j]!=i:
                    return False

            mp_s_t[i]=j
            mp_t_s[j]=i

        
        return True

        