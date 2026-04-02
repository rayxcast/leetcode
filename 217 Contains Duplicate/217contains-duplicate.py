class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values_dic = {}

        for i in nums:
            if i in values_dic:
                return True # return true since we just need any value to appear at least twice
            else:
                values_dic[i] = 1
        
        return False