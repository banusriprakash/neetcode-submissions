class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        mp=defaultdict(list)

        for s in strs:
            ch="".join(sorted(s))

            print(ch)

            mp[ch].append(s)
            print(mp[ch])

            

        return list(mp.values())


        