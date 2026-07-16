class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp=defaultdict(list)

        for ind,val in enumerate(nums):
            mp[val].append(ind)

        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in mp:
                return [i,mp[diff][0]] 

        return [0,0]
        