class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        ans=set()
        j=0
        l1,l2=len(nums1),len(nums2)

        if l1>l2:
            while j<l1:
                if nums1[j] in nums2:
                    ans.add(nums1[j])
                j+=1

        if l2>l1:
            while j<l1:
                if nums2[j] in nums1:
                    ans.add(nums2[j])
                j+=1

        return list(ans)