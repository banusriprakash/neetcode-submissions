class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp={}
        for st in strs:
            og=st
            cp="".join(sorted(st))

            if cp in mp:
                mp[cp].append(og)

            else:
                ls=[]
                ls.append(og)
                mp[cp]=ls

        return list(mp.values())

            

            
        