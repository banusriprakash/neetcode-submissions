class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        i=0
        j=len(flowerbed)-1

        while i<j:

            if i==0 or flowerbed[i+1]==1:
                i+=1

            elif j==len(flowerbed)-1 or flowerbed[j-1]==1:
                j-=1
            
            else:
                n-=1
                i+=1
                j-=1

        return n==0

            
            
        