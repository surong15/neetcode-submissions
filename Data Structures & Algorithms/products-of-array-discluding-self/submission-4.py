class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix & suffix
        n = len(nums)
        output = [0]*n
        pre = [0]*n
        suf = [0]*n

        pre[0] = suf[n-1] = 1
        for i in range(1, n, 1):
            pre[i] = nums[i-1]*pre[i-1]
        for j in range(n-2, -1, -1):
            suf[j] = nums[j+1]*suf[j+1]
        for k in range(n):
            output[k] = pre[k]*suf[k]
        
        return output
        