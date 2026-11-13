class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        current_sum = sum(cardPoints[:k])
        maxS = current_sum

        for i in range(1, k + 1):
            current_sum -= cardPoints[k - i]
            current_sum += cardPoints[-i]
            maxS = max(maxS, current_sum)


        return maxS