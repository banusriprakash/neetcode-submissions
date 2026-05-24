class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp={}
        for st in strs:
            org=st
            cp="".join(sorted(st))
            if st in mp:
                mp[cp].append(org)

            else:
                ls=[]
                ls.append(org)
                mp[cp]=ls

        return list(mp.values())

