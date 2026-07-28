class Solution:
    def merge(self,nums,l,m,r):
        rm=m+1
        low=l
        ans=[]
        while l<=m and rm<=r:
            if nums[l]<=nums[rm]:
                ans.append(nums[l])
                l+=1
            else:
                ans.append(nums[rm])
                rm+=1

        while l<=m:
            ans.append(nums[l])
            l+=1

        while rm<=r:
            ans.append(nums[rm])
            rm+=1

        for i in range(len(ans)):
            nums[low+i]=ans[i]
            

    def mergesort(self,nums,l,r):
        if l<r:
            m=(l+r)//2
            self.mergesort(nums,l,m)
            self.mergesort(nums,m+1,r)
            self.merge(nums,l,m,r)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergesort(nums,0,len(nums)-1)
        