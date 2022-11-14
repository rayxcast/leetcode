class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        k = 2
        
        while k*k < x:
            k+=1
        
        if(k*k) > x:    
            return k - 1
        else:
            return k
    
        
        