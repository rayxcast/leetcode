class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSubArray = 0
        currentSub = 0
        for i in range(len(nums)):
            currentSub += nums[i]

            if i == (k-1): # found first subarray of size k
                maxSubArray = (currentSub / k)
            if i > (k-1):
                currentSub -= nums[i-k]
                if (currentSub/k) > maxSubArray:
                    maxSubArray = (currentSub / k)

        
        return maxSubArray
            