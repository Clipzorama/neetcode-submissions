class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N



        if k == 0 or k == N:
            nums[:] = nums

        else:

            left = nums[(0 - k) % N:]


            right = nums[:N - k]

            nums[:] = left + right