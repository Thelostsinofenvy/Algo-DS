nums = [0, 1, 0, 0, 0, 3, 12]

# brute force


def move(nums):
    i = 0
    j = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            i = i+1
        else:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
            j += 1
    return nums


print(move(nums))
