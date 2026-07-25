class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums:
            return []

        mp={}
        ans=[]
        for i in nums:
            mp[i]=mp.get(i,0)+1

        sorted_desc = dict(sorted(mp.items(), key=lambda item: item[1], reverse=True))

        for ke,v in sorted_desc.items():
            if k>0:
                ans.append(ke)
                k-=1
                
        return ans
                

        