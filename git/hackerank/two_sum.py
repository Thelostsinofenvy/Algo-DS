class Solution:
    nums = [2, 7, 11, 15]
    target = 9
    ans = []

    def twoSum(nums, target):
        # brute force
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    one = nums.index(nums[i])
                    two = nums.index(nums[j])
                    break
            ans = one, two
            return ans
    print(twoSum(nums, target))
