from collections import Counter

# time: O(n * m)
# space: O(m)


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        # for each word we check the frequency and see how many times it appears inside of cnt
        for w in words:
            curr_cnt = Counter(w)

            # we get the minimum amount of times since it must be the same number for all the words
            # Counter() returns 0 if key is not present inside of a word (useful)
            for c in cnt:
                cnt[c] = min(cnt[c], curr_cnt[c])
        
        res = []

        for c in cnt:
            for _ in range(cnt[c]):
                res.append(c)
        
        return res


        