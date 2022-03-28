import random

nums = [random.randint(1,10000) for _ in range(10)]
for i in range(1, len(nums)):
    for j in range(len(nums)-i):
        if nums[j] > nums[j+1]:
            nums[j+1], nums[j] = nums[j], nums[j+1]
print(nums)