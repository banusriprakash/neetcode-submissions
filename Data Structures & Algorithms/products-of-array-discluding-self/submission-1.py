class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        r=[1]*len(nums)
        l=[1]*len(nums)

        r[0]=1
        l[len(nums)-1]=1

        for i in range(1,len(nums),1):
            r[i]=r[i-1]*nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            l[j]=l[j+1]*nums[j+1]

        for k in range(len(nums)):
            nums[k]=r[k]*l[k]

        print(nums)
        return nums