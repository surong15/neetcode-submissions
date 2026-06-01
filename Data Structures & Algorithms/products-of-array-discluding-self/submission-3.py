class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division
        product, zeros = 1,  0
        n = len(nums)

        for num in nums:
            if num: 
                product *= num
            else: 
                zeros += 1
        
        if zeros > 1:
            return [0]*n 
        
        output = [1]*n
        for i, c in enumerate(nums):
            if zeros:
                output[i] = 0 if c else product
            else:
                output[i] = product // c

        return output