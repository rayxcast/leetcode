class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Things to know if the target is 6 we know that it will be after 5 in a nondecreasing array, so if after 5 is 7 then there is not need to find continue iterating with the array

        # In a more general form, 
        # - If the current array value is < than target then continue looking
        # - If the current array value is = to target then save the index, and 
        # continue until the current array value is > than target, then save current index - 1 to result 
        # result can initialy be set to [-1,-1] and values will be change if target is found 

        currentIndex = 0
        output = [-1,-1]
        targetFound = False
        arrayLenght = len(nums)

        if arrayLenght == 0:
            return output

        while currentIndex < arrayLenght and nums[currentIndex] <= target:

            if targetFound == False and nums[currentIndex] == target:
                output[0] = currentIndex
                targetFound = True

            if targetFound:
                output[1] = currentIndex

            currentIndex += 1
        
        return output


