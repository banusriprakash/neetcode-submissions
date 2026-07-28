class Solution:


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        swp=False
        n=len(nums)
        
        for i in range(0,n-1):
            swp=False
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swp=True
            if not swp:
                break

        