nums = input()
result = int(nums[0])
for i in range(1, len(nums)):
    result = max(int(nums[i]) + result, int(nums[i]) * result)
print(result)