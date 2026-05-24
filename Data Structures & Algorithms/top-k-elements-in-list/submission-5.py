class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        ans=[]
        for key,val in counter.items():
            if val>=k:
                ans.append(key)

        return ans
        