class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                output[j] *= nums[i]
        return output