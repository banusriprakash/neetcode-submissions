class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp={}
        
        for i in range(0,len(nums),1):
            mp[nums[i]]=mp.get(nums[i],0)+1

        ans=[]

        for key,val in mp.items():
                ans.append([val,key])

        
        ans.sort()

        res=[]

        while len(res) < k:
            res.append(ans.pop()[1])

        return res
        