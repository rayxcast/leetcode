import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        pL = len(potions) - 1
        pair = [0] * len(spells)
        potions.sort()

        for i in range(len(spells)):
            # greater or equal to the celing of the division of success/spells[i]
            target = math.ceil(success/spells[i])

            # binary search in potions
            currT = 0
            l = 0
            r = pL
            while l <= r:
                m = l + ((r - l) // 2)

                # search the right
                if potions[m] < target:
                    l = m + 1
                # search the left
                else:
                    currT = m
                    r = m - 1

            if l > pL:
                pair[i] = 0
            else:
                pair[i] = pL - currT + 1
            

        return pair

