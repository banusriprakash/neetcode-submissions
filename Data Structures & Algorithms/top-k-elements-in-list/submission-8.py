class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        frq=[0]*(max(nums)+1)
        
        for val in nums:
            frq[val]+=1
            

        print()

        for i in range(len(frq)):
            print(f"{i}-{frq[i]}",end=" ")

        ans=[]
        for i in range(len(frq)-1,-1,-1):
            if frq[i]>0 and k>0:
                ans.append(i)
                k-=1
                
        return ans   