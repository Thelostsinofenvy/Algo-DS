nums = [5, 6, 7, 8, 9, 8]
dup = []

# brute force


def duplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    else:
        return False


print(duplicate(nums))


def duplicatesets(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False


print(duplicatesets(nums))
