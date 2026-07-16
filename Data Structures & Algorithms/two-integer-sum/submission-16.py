class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1

        while l<r:
            sm=nums[l]+nums[r]

            if sm==target:
                return[l,r]

            elif abs(sm)>abs(target):
                r-=1
            else:
                l+=1

        return [0,0]