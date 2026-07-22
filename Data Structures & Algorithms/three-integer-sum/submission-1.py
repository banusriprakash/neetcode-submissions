class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res=[]
        for i in range(0,len(nums)-2,1):
            for j in range(i+1,len(nums)-1,1):
                for k in range(len(nums)-1,j,-1):
                    summ=nums[i]+nums[j]+nums[k]
                    if summ==0:
                        ls=[nums[i],nums[j],nums[k]]
                        ls.sort()
                        if ls not in res:
                            res.append(ls)

        return res
        