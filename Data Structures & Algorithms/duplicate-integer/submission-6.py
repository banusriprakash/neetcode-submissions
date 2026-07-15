class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mp={}

        for val in nums:
            mp[val]=mp.get(val,0)+1

        for val in mp.values():
            if val>1:
                return True
        return False