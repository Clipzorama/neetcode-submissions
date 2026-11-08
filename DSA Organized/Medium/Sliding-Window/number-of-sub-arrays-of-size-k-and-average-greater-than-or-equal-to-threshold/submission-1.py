# time: O(n)
# space: O(1) extra space

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # we will drag this to get the next number in average
        left = 0
        counter = 0
        curr_sum = sum(arr[:k])

        avg = curr_sum // k 

        if avg >= threshold:
            counter += 1
        
        for i in range(k, len(arr)):
            curr_sum += arr[i] - arr[left]
            left += 1

            avg = curr_sum // k 

            if avg >= threshold:
                counter += 1

        return counter

        
        