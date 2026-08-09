class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        LCS = 0
        for num in numset:
            if num-1 not in numset:
                length = 1
                
                while num + length in numset:
                    length += 1
                LCS = max(length,LCS) 
        return LCS
                
            
