# time: O(n + m)
# space: O(n)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setter = set()
        res = set()

        for num in nums1:
            setter.add(num)
        
        for num in nums2:
            if num in setter:
                res.add(num)
        
        return list(res)