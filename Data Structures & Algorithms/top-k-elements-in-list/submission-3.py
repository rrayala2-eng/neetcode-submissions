from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}

        for n in nums:
            res[n] = 1 + res.get(n,0)

        heap = []

        for n in res.keys():
            heapq.heappush(heap,(res[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

      
    


    