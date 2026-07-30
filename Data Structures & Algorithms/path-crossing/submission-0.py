class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        x,y=0,0
        v=set()
        v.add((0,0))
        
        
        for d in path[0:]:

            if d=='N':
                y+=1

            if d=='S':
                y-=1

            if d=='E':
                x+=1

            if d=='W':
                x-=1

            if (x,y) in v:
                return True

            v.add((x,y))

        return False
