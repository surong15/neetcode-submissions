class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        # 左邊所有數的乘積
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # 右邊所有數的乘積
        suffix = 1
        for j in range(n-1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]
        
        return output