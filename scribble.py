nums = [1,2,3,4,5,6,7,8]

k = 4

N = len(nums)

left = nums[(0 - k) % N:]

print(left)

right = nums[:N - k]

print(right)

print(left + right)