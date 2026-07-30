class Solution:
    def firstUniqChar(self, s: str) -> int:
        flg=False
        mp=defaultdict(list)
        for i in range(len(s)):
            mp[s[i]].append(i)

        sorted_dict=dict(sorted(mp.items(),key=lambda val:len(val[1])))
        # print(mp)
        print(sorted_dict)

        
        ans=-1
        for val in sorted_dict.values():
            if len(val)==1:
                ans=val[0]
                return ans

        return ans