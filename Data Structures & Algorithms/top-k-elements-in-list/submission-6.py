class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        print(counter)
        ans=counter.most_common(k)
        return [item[0] for item in ans]
        