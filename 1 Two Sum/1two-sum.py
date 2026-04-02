class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dic = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in nums_dic and nums_dic[c] != i:
                return [i, nums_dic[c]]