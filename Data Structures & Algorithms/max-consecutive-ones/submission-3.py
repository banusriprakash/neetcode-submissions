class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        cnt=0

        max_cnt=-sys.maxsize-1

        for l in range(len(nums)):
            
            cnt+=1
            if nums[l]!=1:
                cnt=0

            max_cnt=max(max_cnt,cnt)
            

        return max_cnt