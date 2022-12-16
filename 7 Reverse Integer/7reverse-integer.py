class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rec = self.reverseRec((-1 * x),(len(str(x))-2))
            if rec > (pow(2, 31)-1):
                return 0
            else:
                return -1 * rec
        else:
            rec = self.reverseRec(x,(len(str(x))-1))
            if rec > (pow(2, 31)-1):
                return 0
            else:
                return rec

    def reverseRec(self, x: int, e: int) -> int:
        if x <= 0: 
            return 0
        elif (x % 10) == 0:
            return self.reverseRec((x // 10), e-1)
        else:
            return (x % 10) * pow(10, e) + self.reverseRec((x // 10), e-1)

