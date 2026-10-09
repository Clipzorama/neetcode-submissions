class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mChanges = 0
        count = 0

        for i in range(k):
            if blocks[i] == "W":
                count += 1

        mChanges = count

        for right in range(k, len(blocks)):
            # deleting the outgoing W character as it wont be in the window anymore
            if blocks[right - k] == "W":
                count -= 1
            
            # adding the incoming W character as it would be in the window
            if blocks[right] == "W":
                count += 1
            
            # checking the current windows "W" count to see if its minimum
            mChanges = min(count, mChanges)
        
        return mChanges