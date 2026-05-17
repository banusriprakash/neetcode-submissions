class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_ele=Counter(nums)

        ans=count_ele.most_common(k)
        
        return [item[0] for item in ans]
        