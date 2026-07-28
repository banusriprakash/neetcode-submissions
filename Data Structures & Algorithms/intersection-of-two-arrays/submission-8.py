class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        ans=[]
        
        mp={}

        for val1 in nums1:
            mp[val1]=mp.get(val1,0)+1

        for val2 in nums2:
            if val2 in mp and val2 not in ans:
                ans.append(val2)

            



        return ans