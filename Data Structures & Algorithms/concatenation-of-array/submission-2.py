class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ls=[]

        for i in range(2):
            for j in range(0,len(nums),1):
                ls.append(nums[j])

        return ls
        