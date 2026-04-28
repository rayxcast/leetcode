class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        s = set()
        c = []
        common = 0

        for i in range(len(A)):
            if A[i] in s:
                common += 1
            s.add(A[i])

            if B[i] in s:
                common += 1
            s.add(B[i])

            c.append(common)
            
            if i == len(A)-1:
                break
        
        return c