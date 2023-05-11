class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = 0
        for i in nums:
            total_sum += i

        left_sum = 0
        for i in range(len(nums)):
            if (total_sum - left_sum - nums[i]) == left_sum:
                return i
            else:
                left_sum += nums[i]

        return -1
