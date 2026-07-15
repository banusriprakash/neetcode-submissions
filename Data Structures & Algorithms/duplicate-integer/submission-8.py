class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st={}

        for val in nums:
            if val in st:
                return True
            st[val]=1

        return False
