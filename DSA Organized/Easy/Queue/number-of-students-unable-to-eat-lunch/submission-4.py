class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        hashMap = {}

        if res == 0:
            return 0

        for s in students:
            hashMap[s] = hashMap.get(s, 0) + 1

        for s in sandwiches:
            if hashMap.get(s, 0) > 0:
                hashMap[s] -= 1
                res -= 1
            else:
                return res

        return res
