class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i,num in enumerate(nums):
            if num in comp:
                return [comp[num],i]
            comp[target-num] = i
        return[]