class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for i in range(0,len(nums),1):

            if nums[i] in mp:
                return True

            mp[nums[i]]=1
            


        return False


            
        