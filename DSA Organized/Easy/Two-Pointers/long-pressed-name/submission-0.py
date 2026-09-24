# time: O(n)
# space: O(1)


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        if len(typed) < len(name):
            return False

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i] != typed[j] and i > 0 and typed[j] == name[i - 1]:
                j += 1
            else:
                return False

        if j <= len(typed) and i < len(name):
            return False

        while j < len(typed):
            if name[i - 1] == typed[j]:
                j += 1
            else:
                return False

        
        return True

n = "alex"
t = "aaleex"

nn = "vtkgn"
tt = "vttkgnn"

a = "pyplrz"

b = "ppyypllr"

result = Solution()
print(result.isLongPressedName(n, t))
print(result.isLongPressedName(nn, tt))
print(result.isLongPressedName(a, b))
