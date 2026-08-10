class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        frec = {}
        for i, v in count.items():
            frec[v] = frec.get(v, []) + [i]

        res = []
        for f in range(len(freq)-1, 0, -1):

            freq[f] += frec.get(f, [])

            if len(freq[f]) != 0:
                res += freq[f]
            
            
            if len(res) == k:
                return res



        



