class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        mp={}
        ans=[]
        for val in nums:
            mp[val]=mp.get(val,0)+1

        for key,val in mp.items():
            if val>=k:
                ans.append(key)

        return ans      