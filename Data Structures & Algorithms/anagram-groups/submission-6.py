class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        mp={}

        for s in strs:
            ch="".join(sorted(s))

            print(ch)

            if ch in mp:
                mp[ch].append(s)
                print(mp[ch])

            else:
                ls=[]
                ls.append(s)
                mp[ch]=ls
                print(mp[ch])

        return list(mp.values())


        