class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if not flowerbed:
            return n == 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            else:
                return False

        # Handle the start of the bed (first two elements)
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        i, j, k = 0, 1, 2

        while k < len(flowerbed):
            if flowerbed[i] == flowerbed[j] == flowerbed[k] == 0:
                flowerbed[j] = 1
                n -= 1
            i += 1
            j += 1
            k += 1
        
        # Handle the end of the bed (last two elements)
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            
        return n <= 0