# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        elif guess(n) == 0:
            return n

        l = 0
        r = n

        while True:
            target = (l + r) // 2
            if guess(target) == 0:
                return target
            # target at the left
            elif guess(target) == -1:
                r = target - 1
            # target at the right
            else:
                l = target + 1

        