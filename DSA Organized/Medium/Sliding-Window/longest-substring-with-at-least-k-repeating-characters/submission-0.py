# Longest Substring with At Least K Repeating Characters Problem (SLIDING WINDOW PROBLEM)


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Return the length of the longest substring where every character
        appears at least k times.

        Sliding Window Idea
        -------------------
        A normal sliding window needs a clear rule for when the window
        becomes invalid and should shrink.

        The difficulty with this problem is:

            "Every character must appear at least k times"

        does NOT immediately tell us when to shrink.

        Example:
            window = "aba"
            k = 2

        'b' only appears once, but shrinking immediately would be wrong
        because another 'b' could appear later.

        To solve that problem, we run the sliding window multiple times.

        For each pass, target_unique tells us how many distinct characters
        we are allowing inside the current window.

        Example:
            target_unique = 2

        means:
            "Find the longest valid substring containing exactly
             2 different characters."

        Since the input only contains lowercase English letters,
        there can be at most 26 unique characters.
        """

        res = 0

        # Try every possible number of unique characters.
        #
        # Pass 1:
        #   only allow 1 unique character
        #
        # Pass 2:
        #   allow 2 unique characters
        #
        # ...
        #
        # Pass 26:
        #   allow up to all lowercase letters
        for target_unique in range(1, 27):

            # Frequency map for the CURRENT sliding window.
            #
            # Example:
            # window = "ababb"
            #
            # counts =
            # {
            #     "a": 2,
            #     "b": 3
            # }
            counts = {}

            # Number of distinct characters currently inside the window.
            #
            # Example:
            # window = "ababb"
            #
            # unique = 2
            # because we have 'a' and 'b'
            unique = 0

            # Number of distinct characters whose frequency has reached k.
            #
            # Example:
            # k = 2
            #
            # counts = {
            #     "a": 2,
            #     "b": 3,
            #     "c": 1
            # }
            #
            # at_least_k = 2
            #
            # because 'a' and 'b' satisfy the requirement,
            # but 'c' does not.
            at_least_k = 0

            # Left boundary of our sliding window.
            left = 0

            # right expands the window one character at a time.
            for right in range(len(s)):

                char = s[right]

                # -----------------------------------------------------
                # STEP 1: EXPAND THE WINDOW
                # -----------------------------------------------------
                #
                # Add s[right] into our current window.
                #
                # Example:
                #
                # before:
                #   counts = {"a": 2}
                #
                # char = "b"
                #
                # after:
                #   counts = {"a": 2, "b": 1}
                counts[char] = counts.get(char, 0) + 1

                # If the count became exactly 1, this character did not
                # previously exist inside the window.
                #
                # Therefore, we gained a new unique character.
                if counts[char] == 1:
                    unique += 1

                # If the character's count JUST reached k,
                # then this character now satisfies the problem's rule.
                #
                # Example:
                # k = 3
                #
                # "a": 2 -> "a": 3
                #
                # 'a' now becomes one of our at_least_k characters.
                #
                # We specifically check == k instead of >= k because
                # we only want to count this milestone once.
                if counts[char] == k:
                    at_least_k += 1

                # -----------------------------------------------------
                # STEP 2: SHRINK THE WINDOW IF NECESSARY
                # -----------------------------------------------------
                #
                # target_unique is the maximum number of different
                # characters allowed during THIS pass.
                #
                # If we have too many unique characters, the window
                # violates our current sliding-window rule.
                #
                # Therefore, move left forward until the window is valid.
                while unique > target_unique:

                    left_char = s[left]

                    # We are about to remove one occurrence of left_char.
                    #
                    # If its count is currently exactly k, removing one
                    # will make it drop BELOW k.
                    #
                    # Example:
                    #
                    # k = 2
                    # "a": 2 -> "a": 1
                    #
                    # 'a' was satisfying the requirement before removal,
                    # but it will no longer satisfy it afterward.
                    if counts[left_char] == k:
                        at_least_k -= 1

                    # Remove the left-most character from the window.
                    counts[left_char] -= 1

                    # If its count becomes zero, that character no longer
                    # exists anywhere inside the current window.
                    #
                    # Therefore, the number of unique characters decreases.
                    if counts[left_char] == 0:
                        unique -= 1

                    # Slide the left boundary forward.
                    left += 1

                # -----------------------------------------------------
                # STEP 3: CHECK WHETHER THE CURRENT WINDOW IS VALID
                # -----------------------------------------------------
                #
                # Example:
                #
                # target_unique = 3
                #
                # counts =
                # {
                #     "a": 3,
                #     "b": 2,
                #     "c": 2
                # }
                #
                # unique = 3
                # at_least_k = 3
                #
                # This means:
                #
                #   - we have exactly 3 unique characters
                #   - all 3 appear at least k times
                #
                # Therefore, every character inside the window satisfies
                # the requirement.
                if unique == target_unique and unique == at_least_k:

                    # Sliding window length formula:
                    #
                    # Example:
                    #
                    # left = 2
                    # right = 6
                    #
                    # indices:
                    # 2, 3, 4, 5, 6
                    #
                    # length = 6 - 2 + 1 = 5
                    window_length = right - left + 1

                    res = max(res, window_length)

        return res


# ---------------------------------------------------------
# EXAMPLES
# ---------------------------------------------------------

result = Solution()

print(result.longestSubstring("aaabb", 3))
# Output: 3
#
# Longest valid substring:
# "aaa"
#
# a -> 3 times


print(result.longestSubstring("ababbc", 2))
# Output: 5
#
# Longest valid substring:
# "ababb"
#
# a -> 2 times
# b -> 3 times


print(result.longestSubstring("abaaccbb", 2))
# Output: 8
#
# The entire string is valid:
#
# a -> 3
# b -> 3
# c -> 2
#
# Every character appears at least 2 times.