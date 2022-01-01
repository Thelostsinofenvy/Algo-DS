class Solution:
    def maxSubArray(self, nums):
        # initialize 0 and first val in array
        curr_sub = 0
        max_sub = nums[0]

        # iterate thru nums
        for x in nums:
            # if running sum less than 0, reset to 0
            if curr_sub < 0:
                curr_sub = 0
            # sum
            curr_sub += x

            # if running sum > max sum, take higher val
            max_sub = max(curr_sub, max_sub)

        return max_sub
