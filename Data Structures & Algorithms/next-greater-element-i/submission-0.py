class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans=[-1]*len(nums1)
        for i in range(len(nums1)):
            si=nums2.index(nums1[i])
            for j in range(si+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break
        
        return ans
        