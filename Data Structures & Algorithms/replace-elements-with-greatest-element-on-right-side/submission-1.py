class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            # This is a good way to check if the loop variable hit the last element   
            #in the iterable
            if i != len(arr) - 1:
                arr[i] = max(arr[i + 1:])
            else:
                arr[-1] = -1

        return arr