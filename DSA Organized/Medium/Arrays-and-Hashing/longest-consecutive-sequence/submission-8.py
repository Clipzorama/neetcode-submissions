class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setter = set(nums)
        longest = 0

        for n in setter:

            if (n - 1) not in setter:
                streak = 0

                while (n + streak) in setter:
                    streak += 1
                    longest = max(longest, streak)            
        
        return longest



        


        