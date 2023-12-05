class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, (len(numbers)-1)

        while l < r:
            t = target - numbers[l]
            if numbers[r] == t:
                return [l+1, r+1]
            elif numbers[r] > t:
                r-=1
            else:
                l+=1
        