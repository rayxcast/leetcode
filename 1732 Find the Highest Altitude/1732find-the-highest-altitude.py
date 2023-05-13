class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_array = []
        prefix_array.append(0)

        max_alt = 0
        for i in range(len(gain)):
            prefix_array.append(prefix_array[i] + gain[i])
            max_alt = max(prefix_array[i+1], max_alt) 

        return max_alt