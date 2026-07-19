class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wr=0

        for r in range(len(nums)):
            if nums[r]!=val:
                nums[wr]=nums[r]
                wr+=1
            
        return wr
        