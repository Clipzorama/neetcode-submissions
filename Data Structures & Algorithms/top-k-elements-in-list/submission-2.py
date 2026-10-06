from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = dict(Counter(nums))

        sorted_nums = sorted(d, key=d.get, reverse=True)

        return sorted_nums[:k]