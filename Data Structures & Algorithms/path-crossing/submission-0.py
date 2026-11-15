class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            'N':(0,1),
            'S':(0,-1),
            'E':(1,0),
            'W':(-1,0)
        }

        currX , currY = 0 , 0
        seen = set()
        seen.add((currX,currY))

        for p in path:
            newX , newY = directions[p]
            currX += newX
            currY += newY
            if (currX,currY) in seen:
                return True
            seen.add((currX,currY))
        
        return False