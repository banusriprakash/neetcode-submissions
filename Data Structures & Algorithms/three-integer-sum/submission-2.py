class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        nums.sort()
        for i in range(0,len(nums)-2,1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j=i+1
            k=len(nums)-1

            while j<k:
                summ=nums[i]+nums[j]+nums[k]

                if summ>0:
                    k-=1
                elif summ<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    
                
                

        return res
        