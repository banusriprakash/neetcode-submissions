class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)-1,1):
            minIndex=i
            for j in range(i+1,len(nums),1):
                if nums[minIndex]>nums[j]:
                    minIndex=j

            tmp=nums[minIndex]
            nums[minIndex]=nums[i]
            nums[i]=tmp

        return nums