class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(0,len(nums)-1,1):
            for j in range(i+1,len(nums),1):
                if nums[i]>nums[j]:
                    a=nums[i]
                    nums[i]=nums[j]
                    nums[j]=a

        print(nums)

        return nums
        