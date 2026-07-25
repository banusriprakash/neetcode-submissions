class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i,j=0,0
        len1,len2=len(nums1),len(nums2)
        m1,m2=0,0
        for c in range((len1+len2)//2+1):
            m2=m1
            if i<len1 and j<len2:
                if nums1[i]>nums2[j]:
                    m1=nums2[j]
                    j+=1
                else:
                    m1=nums1[i]
                    i+=1
            elif i<len1:
                m1=nums1[i]
                i+=1

            else:
                m1=nums[j]
                j+=1

        
        if (len1+len2)%2==1:
            return float(m1)

        else:
            return (m1+m2)/2.0


        