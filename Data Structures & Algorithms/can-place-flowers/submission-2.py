class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n==0 and (len(flowerbed)%2==1):
            return True

        cnt=n

        i=0
        j=i+2
        ln=len(flowerbed)

        while i<ln and j<ln:
            if flowerbed[i]==1 and flowerbed[j]==0:
                i+=1
                j+=2
                cnt-=1

            elif flowerbed[i]==0 and flowerbed[j]==1:
                i+=1
                j+=1
                cnt-=1

            elif cnt<=0:
                return True
            
            
        return cnt!=0
        