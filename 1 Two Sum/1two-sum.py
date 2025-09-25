class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Let's create a set for fast checking
        arrMap = {value: index for index, value in enumerate(nums)}
        # print("arrMap:", arrMap)
        output = []
        for index, n in enumerate(nums):
            # print("index, n:", index, n)
            complement = target-n
            # print("complement:", complement)
            if complement in arrMap and arrMap[complement] != index:
                output.extend([index, arrMap[complement]])
                break
        
        return output