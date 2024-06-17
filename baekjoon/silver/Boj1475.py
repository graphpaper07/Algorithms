N = input()
nums = [0] * 10
for elem in N:
    nums[int(elem)] += 1

nums[6] += nums[9]
nums[9] = 0
nums[6] = nums[6] // 2 + nums[6] % 2
print(max(nums))