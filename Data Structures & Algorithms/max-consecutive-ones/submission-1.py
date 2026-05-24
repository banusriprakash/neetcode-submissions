class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        st=set()
        cnt=0
        maxi=1
        for num in nums:
            if num==1:
                cnt+=1
                maxi=max(cnt,maxi)
            else:
                cnt=0

        return max(cnt,maxi)

            
