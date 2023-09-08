class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Using pointers
        l = 0
        r = len(height) - 1
        maxWater = 0
        while(l<r):
            currWater = min(height[l], height[r]) * (r-l)
            if currWater > maxWater:
                maxWater = currWater

            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        
        return maxWater
        