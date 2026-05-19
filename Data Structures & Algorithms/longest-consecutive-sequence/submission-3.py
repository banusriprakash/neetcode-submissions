class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set()

        if not nums:
            return 0

        for num in nums:
            st.add(num)

        print(st)

        cnt=1

        maxi=1
        arr=sorted(list(st))
        for i in range(1,len(arr),1):
            if arr[i]==arr[i-1]+1:
                cnt+=1

            else:
                maxi=max(cnt,maxi)
                cnt=1

        print(maxi)   
        maxi = max(cnt, maxi)
        return maxi
        
