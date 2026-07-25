class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False

        l=len(flowerbed)-1

        for i in range(l):
            if flowerbed[i]==0:
                em_l=(i==0) or (flowerbed[i-1]==0)
                em_r=(i==l-1) or (flowerbed[i+1]==0)

                if em_l and em_r:
                    flowerbed[i]=1
                    n-=1

                    if n==0:
                        return True
        

        return n==0

            
            
        