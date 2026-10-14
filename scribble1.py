def productExceptSelf(nums: list[int]) -> list[int]:
    ans = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans



n = [3, 2, 5, 4, 6]

print(productExceptSelf(n))