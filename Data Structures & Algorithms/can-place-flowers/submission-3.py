class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n==0 and (len(flowerbed)%2==1):
            return True

        cnt=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                cnt+=1 
                
        rem=cnt%n
        if n>cnt:
            rem=n%cnt
        return rem==0
        