from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = 0
        count = Counter(arr)

        for key, value in count.items():
            if value == 1:
                distinct += 1
            
            if distinct == k:
                return key
        

        return ""


        