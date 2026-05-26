class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, v in enumerate(nums):
            arr.append([i, v])
        l = 0
        r = len(nums)-1
        arr.sort(key = lambda x: x[1])
        while (l!=r):
            sum = arr[l][1]+arr[r][1]
            if sum < target:
                l = l+1
                continue
            elif (sum > target):
                r = r-1
                continue
            else: 
                ans = [arr[l][0], arr[r][0]]
                ans.sort()
                return ans

        