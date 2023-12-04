class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # pre-conditions: given integer array
        # post-contidions: return False if each value in the array is distint else return True

        # Design idea:
        # Using a for loop to check each integer in the array and using a set to check if the element exist

        # Termination: after going through all the elements in the array

        # if len(set(nums)) < len(nums):
        #     return True
        
        # return False

        # for i in nums:
        #     if i not in s:
        #         s.add(i)
        #     else:
        #         return True

        # return False

        hm = dict()

        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                return True
        
        return False

        # Memory complexity of at least O(n)
        # Time complexiy is O(n)

        