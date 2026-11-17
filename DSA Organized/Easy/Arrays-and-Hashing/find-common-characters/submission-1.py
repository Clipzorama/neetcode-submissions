# a solution without using counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # first frequency count of letters for the first word
        cnt = {}

        for c in words[0]:
            cnt[c] = cnt.get(c, 0) + 1
        
        # after for each word, we get the frequency for each word and then calulate the minimum
        for w in words:
            curr_cnt = {}
            # thats what were doing here
            for c in w:
                curr_cnt[c] = curr_cnt.get(c, 0) + 1
            
            # and this is obviously the most important part
            for c in cnt:
                cnt[c] = min(cnt[c], curr_cnt.get(c, 0))
        
        # then the same as the other solution
        res = []
        for c in cnt:

            for _ in range(cnt[c]):
                res.append(c)

        return res
         

        