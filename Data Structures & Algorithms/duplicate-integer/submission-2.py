class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for i in range(0,len(nums),1):
            mp[nums[i]]=mp.get(nums[i],0)+1

        for val in mp.values():
            if val>1:
                return True

        return False


            
        