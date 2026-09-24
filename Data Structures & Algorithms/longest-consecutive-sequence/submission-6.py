class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setter = set(nums)
        maxStreak = 0
        length = 0

        for n in setter:

            if (n - 1) not in setter:
                streak = 0
                length = 0
                
                while (n + length) in setter:
                    streak += 1
                    length += 1

                    maxStreak = max(maxStreak, streak)
        
        return maxStreak

        