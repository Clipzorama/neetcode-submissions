class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        denials = 0
        while denials != len(students) and students:
            chosen = students.pop(0)
            if chosen == sandwiches[0]:
                denials = 0
                sandwiches.pop(0)
            else:
                denials += 1
                students.append(chosen)


        return len(students)
