class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        output = []
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            output.append(sm)

        return output
