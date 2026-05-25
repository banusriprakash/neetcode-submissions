from typing import List

class Solution:
    def merge(self, l: int, m: int, h: int, nums: List[int]) -> None:
        left, right = l, m + 1
        ans = []
        
        # FIX 1: Check bounds against m and h, not against each other
        while left <= m and right <= h:
            if nums[left] <= nums[right]:
                ans.append(nums[left])
                left += 1
            else:
                ans.append(nums[right])
                right += 1
            
        while left <= m:
            ans.append(nums[left])
            left += 1

        while right <= h:
            ans.append(nums[right])
            right += 1

        # FIX 2: Use l (not low), and add i to l to move forward
        for i in range(len(ans)):
            nums[l + i] = ans[i]

    def mergesort(self, l: int, r: int, nums: List[int]) -> None:
        if l >= r:
            return
            
        m = (l + r) // 2
        
        self.mergesort(l, m, nums)
        # FIX 3: Start at m + 1, and use r (since h is not defined here)
        self.mergesort(m + 1, r, nums) 
        self.merge(l, m, r, nums)
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergesort(0, len(nums) - 1, nums)
        
        # FIX 4: Removed "return nums" to satisfy the in-place requirement