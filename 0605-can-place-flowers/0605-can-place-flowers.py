class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            # Agar current jaga khaali ho
            if flowerbed[i] == 0:
                # left side khaali ya list ka start ho
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                # right side khaali ya list ka end ho
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1  # yahan flower laga do
                    n -= 1  # ek flower lag gaya

                    if n == 0:
                        return True  # kaam ho gaya
        return n <= 0  # agar sab flowers lag gaye hon to True, warna False
