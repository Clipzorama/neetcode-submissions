from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1

        for num in arr:
            if num == cnt[num]:
                res = max(res, num)
        
        return res
        