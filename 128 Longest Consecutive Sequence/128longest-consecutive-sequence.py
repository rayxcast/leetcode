class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # dic = {n:set() for n in nums}
        
        # for n in nums:
        #     if n+1 in dic:
        #         # dic[n].add(n)
        #         dic[n].add(n+1)
        # # print(dic)
        # l = {}
        # # dic = dict(sorted(dic.items()))
        # print(dic)
        # for n in dic:
        #     if not n in l:
        #         l[n] = len(dic[n])
        #     if n-1 in dic:
        #         l[n] = len(dic[n]) + l[n-1]

        # print(l)
        # print(dic)

        # largest = 0
        # for seq in l.values():
        #     if seq > largest:
        #         largest = seq

        # return largest+1

        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if n is the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest