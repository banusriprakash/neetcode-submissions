class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        st=set()
        
    

        for val1 in nums1:
            for val2 in nums2:
                if val1==val2:
                    st.add(val1)




        return list(st)