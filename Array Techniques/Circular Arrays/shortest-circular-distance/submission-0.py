class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        minCount = float("inf")
        N = len(words)
        counterR = 1
        counterL = 1
        flagger = startIndex

        # initial condition to check if this works 
        if target not in words:
            return -1
        
        if words[startIndex] == target:
            return 0


        for i in range(startIndex, 2 * N):

            if words[(i + 1) % N] == target:
                minCount = min(minCount, counterR)
                counterR -= 1

            counterR += 1

            if words[(flagger - 1 + N) % N] == target:
                minCount = min(minCount, counterL)
                counterL -= 1
                flagger = startIndex
            
            counterL += 1
            flagger -= 1
        
        return minCount






# Output: 1

# w = ["hello","i","am","leetcode","hello"]
# t = "hello"
# s = 1


ww = ["wrjvjb","wrjvjb","zgmjbq","mkqeuk","aevhdp","zgmjbq"]
tt = "wrjvjb"
ss = 4
result = Solution()
# print(result.closestTarget(w, t, s))
print(result.closestTarget(ww, tt, ss))





# theres also another solution thats a bit more optimal than this


def closestT(words: list[str], target: str, startIndex: int) -> int:
        N = len(words)

        for distance in range(len(words)):

            left = (startIndex - distance) % N

            right = (distance + startIndex) % N

            if words[left] == target or words[right] == target:
                return distance
        

        return -1