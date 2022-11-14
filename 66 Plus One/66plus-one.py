class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        # Worst case we go though the whole array
        # Best case we add 1 only to the least significant digit
        while i >= 0:
            # if the current digit is 9
            if digits[i] == 9: 
                # if the digit isn't the MSB
                if i > 0: 
                    # set digit to 0 add one to the next
                    digits[i] = 0
                # if the digit is the MSB
                elif i == 0:
                    # set digit to 0
                    digits[i] = 0
                    # add a digit of 1 to the array at MSB
                    digits.insert(0, 1)
            else:
                # else just need to add 1 to the LSB
                digits[i] = digits[i] + 1
                break
            i-=1
        
        return digits