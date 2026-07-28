class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        st=set()
        
    

        for val in nums2:
            if val in nums1:
                st.add(val)
    
        return list(st)




        return list(ans)