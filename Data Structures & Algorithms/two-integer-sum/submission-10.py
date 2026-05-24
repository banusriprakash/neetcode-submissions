class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        ans=[]

        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in mp:
                ans.append(mp[rem])
                ans.append(i)

            mp[nums[i]]=i

        return ans