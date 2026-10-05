# ============================================================
# CIRCULAR ARRAYS
# ============================================================
#
# A circular array behaves like the end connects back
# to the beginning.
#
# Example:
#
# [10, 20, 30, 40]
#
# After 40, we wrap back to 10.
#
# Conceptually:
#
# 10 -> 20 -> 30 -> 40
# ^                 |
# |_________________|
#
# Circular arrays commonly use MODULO (%) to wrap indices.
# ============================================================


nums = [10, 20, 30, 40]
N = len(nums)


# ============================================================
# 1. BASIC WRAPAROUND WITH MODULO
# ============================================================

# Normal indices:
#
# 0 -> 10
# 1 -> 20
# 2 -> 30
# 3 -> 40
#
# But index 4 does not normally exist.
#
# Using:
#
# index % N
#
# wraps the index back into the valid range.


print(0 % N)   # 0
print(1 % N)   # 1
print(2 % N)   # 2
print(3 % N)   # 3
print(4 % N)   # 0  -> wraps back to beginning
print(5 % N)   # 1
print(6 % N)   # 2


# ============================================================
# 2. ACCESSING VALUES PAST THE END
# ============================================================

# Instead of:
#
# nums[index]
#
# use:
#
# nums[index % N]
#
# when you want circular behavior.


for i in range(8):
    print(nums[i % N])

# Output:
#
# 10
# 20
# 30
# 40
# 10
# 20
# 30
# 40


# ============================================================
# 3. GET THE NEXT ELEMENT
# ============================================================

i = 3

# i is currently pointing at 40.
#
# Normally:
#
# i + 1 = 4
#
# But index 4 does not exist.
#
# Modulo wraps 4 back to 0.

next_index = (i + 1) % N

print(nums[next_index])  # 10


# Pattern:
#
# next index
# (i + 1) % N


# ============================================================
# 4. GET THE PREVIOUS ELEMENT
# ============================================================

i = 0

# The element before index 0 should be the last element.
#
# Python modulo also handles negative values nicely:
#
# (-1) % 4 = 3

previous_index = (i - 1) % N

print(nums[previous_index])  # 40


# Pattern:
#
# previous index
# (i - 1) % N


# ============================================================
# 5. MOVE MULTIPLE STEPS FORWARD
# ============================================================

i = 2
steps = 3

# Start:
#
# index 2 -> 30
#
# Move 3 steps:
#
# 30 -> 40 -> 10 -> 20
#
# Final index should be 1.

new_index = (i + steps) % N

print(nums[new_index])  # 20


# Pattern:
#
# move forward k positions
# (i + k) % N


# ============================================================
# 6. MOVE MULTIPLE STEPS BACKWARD
# ============================================================

i = 1
steps = 3

# Start:
#
# index 1 -> 20
#
# Move backward 3:
#
# 20 -> 10 -> 40 -> 30

new_index = (i - steps) % N

print(nums[new_index])  # 30


# Pattern:
#
# move backward k positions
# (i - k) % N


# ============================================================
# 7. NEXT K ELEMENTS
# ============================================================

nums = [5, 7, 1, 4]
N = len(nums)

i = 2
k = 3

# Current element:
#
# nums[2] = 1
#
# Next 3 values:
#
# 4
# 5   <- wrapped around
# 7

for step in range(1, k + 1):
    index = (i + step) % N
    print(nums[index])


# General pattern:
#
# for step in range(1, k + 1):
#     nums[(i + step) % N]


# ============================================================
# 8. PREVIOUS K ELEMENTS
# ============================================================

i = 1
k = 3

# Current:
#
# nums[1] = 7
#
# Previous 3:
#
# 5
# 4   <- wrapped backward
# 1

for step in range(1, k + 1):
    index = (i - step) % N
    print(nums[index])


# General pattern:
#
# for step in range(1, k + 1):
#     nums[(i - step) % N]


# ============================================================
# 9. WHY MODULO WORKS
# ============================================================

# If:
#
# N = 4
#
# valid indices are:
#
# 0 1 2 3
#
#
# Modulo forces any positive index back into:
#
# 0 <= index < N
#
#
# Examples:
#
# 4 % 4 = 0
# 5 % 4 = 1
# 6 % 4 = 2
# 7 % 4 = 3
# 8 % 4 = 0
#
#
# So the pattern repeats forever:
#
# 0 1 2 3 0 1 2 3 0 1 2 3 ...


# ============================================================
# 10. CIRCULAR ARRAYS + SLIDING WINDOW
# ============================================================

# Circular-array problems are often combined with sliding window.
#
# Example:
#
# nums = [5, 7, 1, 4]
#
# Suppose we want windows of size 3.
#
# Conceptually, imagine the array repeated:
#
# [5, 7, 1, 4, 5, 7, 1, 4]
#
# But instead of actually copying the array, we can do:
#
# nums[r % N]
#
#
# r:
#
# 0 -> nums[0]
# 1 -> nums[1]
# 2 -> nums[2]
# 3 -> nums[3]
# 4 -> nums[0]
# 5 -> nums[1]
#
#
# This is exactly what happens in problems like:
#
# Defuse the Bomb


# ============================================================
# 11. COMMON CIRCULAR ARRAY PATTERNS
# ============================================================


# Next element
next_index = (i + 1) % N


# Previous element
previous_index = (i - 1) % N


# Move k steps forward
forward = (i + k) % N


# Move k steps backward
backward = (i - k) % N


# Access while looping past the end
value = nums[i % N]


# ============================================================
# 12. PATTERN RECOGNITION
# ============================================================

# Think CIRCULAR ARRAY when the problem says things like:
#
# - "wrap around"
# - "after the last element, continue from the first"
# - "before the first element is the last element"
# - "next k elements in a circular array"
# - "previous k elements"
# - "clockwise / counterclockwise"
# - "cyclic"
# - "ring"
#
#
# Your immediate thought should be:
#
#            INDEX % N
#
#
# Forward:
#
# (i + something) % N
#
#
# Backward:
#
# (i - something) % N


# ============================================================
# QUICK CHEAT SHEET
# ============================================================

# N = len(nums)

# next:
# nums[(i + 1) % N]

# previous:
# nums[(i - 1) % N]

# k forward:
# nums[(i + k) % N]

# k backward:
# nums[(i - k) % N]

# loop beyond array:
# nums[i % N]