class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # seq = [None] * (n+1)

        # seq[0] = 0
        # seq[1] = 1
        # seq[2] = 1

        one = 0  
        two = 1 
        three = 1  
        val = 0

        for i in range(3, n+1):
            val = one + two + three
            one = two
            two = three
            three = val

        return val

        