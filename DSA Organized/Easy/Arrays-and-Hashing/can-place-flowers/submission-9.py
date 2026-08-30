class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fit = 0

        if n == 0:
            return True


        for i in range(len(flowerbed)):
            # if current position is 0, we test
            if flowerbed[i] == 0:
                # checking both left and right boundaries
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                # both must be true to satisfy condition
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    fit += 1

                    if fit == n:
                        return True

        return fit == n