value = input()
value = value.split("-")
total = 0
for nums in value[0].split("+"):
    total += int(nums)
for nums in value[1:]:
    for num in nums.split("+"):
        total -= int(num)
print(total)
