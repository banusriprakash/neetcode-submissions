class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        mp=defaultdict(list)

        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
                print(count)
            mp[tuple(count)].append(s)

            

        return list(mp.values())


        