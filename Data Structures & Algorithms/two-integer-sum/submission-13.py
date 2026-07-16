class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp={}

        for ind,val in enumerate(nums):
            mp[val]=ind

        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in mp:
                return[i,mp[diff]]

        return [0,0]
        