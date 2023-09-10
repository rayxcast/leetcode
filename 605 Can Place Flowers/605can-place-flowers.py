class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n == 0:
            return True
            
        while(i < len(flowerbed)):
            l = True
            r = True
            if flowerbed[i] == 0:
                if i-1 >= 0:
                    if flowerbed[i-1] != 0:
                        l = False
                if i+1 < len(flowerbed):
                    if flowerbed[i+1] != 0:     
                        r = False
                
                if l and r:
                    flowerbed[i] = 1
                    n-=1
                
                if n == 0:
                    return True
            
            i += 1
        
        return False