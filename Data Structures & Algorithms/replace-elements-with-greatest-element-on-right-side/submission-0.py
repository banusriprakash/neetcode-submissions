class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_val=-sys.maxsize-1

        for i in range(len(arr)-1,-1,-1):
            curr_val=arr[i]
            
            arr[i]=max_val
            max_val=max(max_val,curr_val)

        arr[len(arr)-1]=-1
        return arr
        