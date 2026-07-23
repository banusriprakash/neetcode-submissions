class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        i=0
        min_area=-sys.maxsize-1
        res=0
        for j in range(i+1,len(heights)):
            min_area=min(heights[i],heights[j])
            res=max((j-i)*min_area,res)

            if heights[i]<heights[j]:
                i+=1

        return res
            

        