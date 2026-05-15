class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        ans=[]
        for i in range(0,len(nums),1):
            rem=target-nums[i]
            if rem in mp:
                ans.append(mp[rem])
                ans.append(i)
                
                break

            mp[nums[i]]=i

        return ans

