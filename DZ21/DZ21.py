def count_negative(nums):
    if not nums:
        return 0
    if nums[0] < 0:
        return 1 + count_negative(nums[1:])
    else:
        return count_negative(nums[1:])

numbers = [-2, 3, 8, -11, -4, 6]
n = count_negative(numbers)

print(numbers)
print(f"n = {n}")
