class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate the prefix products.
        prefix_product = 1
        for i in range(len(nums)):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate the suffix products.
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer