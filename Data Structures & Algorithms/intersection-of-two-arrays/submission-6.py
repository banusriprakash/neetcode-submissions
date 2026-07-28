class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        ans=[]
        
    

        for val1 in nums1:
            for val2 in nums2:
                if val1==val2:
                    if val1 not in ans:
                        ans.append(val1)




        return ans