class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0)+1
        out = []
        for num , count in hmap.items():
            if len(out) < k:
                out.append(num)
            else:
                # Find the least frequent element currently in out
                min_idx = 0
                for i in range(1, k):
                    if hmap[out[i]] < hmap[out[min_idx]]:
                        min_idx = i

                if hmap[num] > hmap[out[min_idx]]:
                    out[min_idx] = num
        return out
                

        