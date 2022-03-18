def add_evens(nums):
    sum = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            sum += nums[i]
    return sum