class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1

        l = len(nums)
        for i in range(l):
            if right < l:
                if nums[left] == 0 and nums[right] != 0:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
                elif nums[left] != 0:
                    left += 1
                right += 1