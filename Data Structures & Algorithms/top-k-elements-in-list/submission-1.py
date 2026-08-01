import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0)+1
        heap = []
        for num , count in hmap.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count,num in heap]
                

        