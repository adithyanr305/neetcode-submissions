class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def prod(lis):
            mul = 1
            for i in lis:
                mul *= i   
            return mul

        ans = []
        for i in range(len(nums)):
            l = prod(nums[:i])
            r = prod(nums[i+1:])
            ans.append(l*r)
        return ans