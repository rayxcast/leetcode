class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dic = {}
        for n in nums:
            if n in freq_dic:
                freq_dic[n] += 1
            else:
                freq_dic[n] = 1
  
        # print(freq_dic)
        arr = sorted(freq_dic.items(), key=lambda item: -item[1])

        # print(arr)
        f_arr = []
        for i in range(k):
            f_arr.append(arr[i][0])

        # print(f_arr)

        return f_arr