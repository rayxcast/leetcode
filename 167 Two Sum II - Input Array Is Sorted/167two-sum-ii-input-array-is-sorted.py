class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1

        while l < r:
            find = target - numbers[l]
            if numbers[r] == find:
                return [l+1, r+1]
            if numbers[r] < find:
                l += 1
            else:
                r -= 1
        