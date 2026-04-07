class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # nums = sorted(nums)
        # dic = {nums[i]:i for i in range(len(nums))}
        # l = 0
        # r = len(nums) - 1
        # arr = {}
        # print(nums)
        # while l < r:
        #     target = (nums[l]+nums[r]) * -1
        #     print(target, (l, r))
        #     if target in dic and dic[target] != l and dic[target] != r:
        #         key = (nums[l], target, nums[r])
        #         if target > nums[r]:
        #             key = (nums[l], nums[r], target)
        #         elif target < nums[l]:
        #             key = (target, nums[l], nums[r])
        #         arr[key] = 1
        #     if nums[r] < target:
        #         l += 1
        #     else:
        #         r -= 1
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0
        
        for x in nums:
            if x < 0:
                neg[x] += 1
            elif x > 0:
                pos[x] += 1
            else:
                zeros += 1
        
        r = []
        
        if zeros:
            for n in neg:
                if -n in pos:
                    r.append((0, n, -n))
        
            if zeros > 2:
                r.append((0,0,0))

        for set_a, set_b in ((neg, pos), (pos, neg)):
            set_a_items = list(set_a.items())
            for i, (x, q) in enumerate(set_a_items):
                for x2, q2 in set_a_items[i:]:
                    if x != x2 or (x == x2 and q > 1):
                        if -x-x2 in set_b:
                            r.append((x, x2, -x-x2))

        return r
        
        # return [list(st) for st in arr]