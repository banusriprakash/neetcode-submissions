class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False

        if len(flowerbed)==1 and n==1 and flowerbed[0]==0:
            return True

        i=0
        j=len(flowerbed)-1

        while i<j:

            if i==0 and flowerbed[i+1]==0:
                i+=1

            elif j==len(flowerbed)-1 and flowerbed[j-1]==0:
                j-=1
            
            else:
                n-=1
                i+=1
                j-=1

        return n==0

            
            
        