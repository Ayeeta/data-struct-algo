class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
    
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
    
        flowercount = n
    
        for i in range(len(flowerbed)):
        
        
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    flowercount -= 1
    
        
            elif i == len(flowerbed) - 1: 
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    flowercount -= 1
        
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and                            flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    flowercount -= 1
        
            if flowercount == 0:
                return True
            
        return False
            