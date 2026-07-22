class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1,-1]
        mp={}

        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in mp:
                return [mp[diff]+1,i+1]

            mp[numbers[i]]=i

        return [-1,-1]